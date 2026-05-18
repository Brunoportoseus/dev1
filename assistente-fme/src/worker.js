// Assistente de IA "Tutor FME" — Cloudflare Worker.
// Serve a interface de chat (GET /) e responde perguntas em streaming
// (POST /api/chat), fundamentado na base de conhecimento do FME.
// A chave da API fica no segredo ANTHROPIC_API_KEY (nunca vai ao navegador).

import Anthropic from "@anthropic-ai/sdk";
import { BASE_CONHECIMENTO, PERSONA } from "./knowledge.js";
import { PAGINA_HTML } from "./ui.js";

const MAX_MSGS = 12; // janela de conversa enviada ao modelo
const MAX_CHARS = 4000; // limite por mensagem do usuário

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "GET" && url.pathname === "/") {
      return new Response(PAGINA_HTML, {
        headers: { "content-type": "text/html; charset=utf-8" },
      });
    }

    if (request.method === "POST" && url.pathname === "/api/chat") {
      return handleChat(request, env);
    }

    return new Response("Não encontrado", { status: 404 });
  },
};

async function handleChat(request, env) {
  if (!env.ANTHROPIC_API_KEY) {
    return json({ error: "Configuração ausente: defina o segredo ANTHROPIC_API_KEY." }, 500);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "Corpo da requisição inválido." }, 400);
  }

  const raw = Array.isArray(body?.messages) ? body.messages : [];
  const messages = raw
    .filter(
      (m) =>
        m &&
        (m.role === "user" || m.role === "assistant") &&
        typeof m.content === "string" &&
        m.content.trim().length > 0,
    )
    .slice(-MAX_MSGS)
    .map((m) => ({ role: m.role, content: m.content.slice(0, MAX_CHARS) }));

  if (messages.length === 0 || messages[messages.length - 1].role !== "user") {
    return json({ error: "Envie ao menos uma pergunta do usuário." }, 400);
  }

  const client = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY });
  const model = env.MODEL || "claude-opus-4-7";

  const stream = client.messages.stream({
    model,
    max_tokens: 2048,
    // Prefixo estável (persona + base de conhecimento) cacheado: as perguntas
    // variam e ficam em `messages`, depois do prefixo cacheado.
    system: [
      {
        type: "text",
        text: `${PERSONA}\n\n---\n\n${BASE_CONHECIMENTO}`,
        cache_control: { type: "ephemeral" },
      },
    ],
    messages,
  });

  const encoder = new TextEncoder();
  const readable = new ReadableStream({
    async start(controller) {
      const send = (obj) =>
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(obj)}\n\n`));
      try {
        for await (const event of stream) {
          if (
            event.type === "content_block_delta" &&
            event.delta.type === "text_delta"
          ) {
            send({ delta: event.delta.text });
          }
        }
        const final = await stream.finalMessage();
        send({
          done: true,
          usage: {
            input: final.usage.input_tokens,
            output: final.usage.output_tokens,
            cache_read: final.usage.cache_read_input_tokens ?? 0,
            cache_write: final.usage.cache_creation_input_tokens ?? 0,
          },
        });
      } catch (err) {
        send({ error: "Falha ao gerar a resposta. Tente novamente." });
      } finally {
        controller.close();
      }
    },
  });

  return new Response(readable, {
    headers: {
      "content-type": "text/event-stream; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

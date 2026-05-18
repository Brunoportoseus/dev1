// Interface de chat servida pelo Worker (HTML autocontido).
export const PAGINA_HTML = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tutor FME — Tire suas dúvidas sobre o Fundo Municipal de Esporte</title>
<style>
  :root{--verde:#1b8a5a;--verde-esc:#0f5c3a;--azul:#1f4e79;--cinza:#5b6770;
    --bg:#eef1f3;--borda:#dce3e9;--bot:#fff;--user:#1b8a5a;}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);
    color:#1d2733;height:100vh;display:flex;flex-direction:column}
  header{background:linear-gradient(135deg,var(--verde-esc),var(--verde));
    color:#fff;padding:16px 22px}
  header h1{font-size:18px;font-weight:800}
  header p{font-size:12.5px;opacity:.9;margin-top:2px}
  main{flex:1;overflow-y:auto;padding:22px;max-width:820px;margin:0 auto;width:100%}
  .msg{display:flex;margin-bottom:16px}
  .msg .b{max-width:80%;padding:12px 16px;border-radius:14px;font-size:15px;
    line-height:1.55;white-space:pre-wrap;word-wrap:break-word}
  .msg.bot .b{background:var(--bot);border:1px solid var(--borda);
    border-bottom-left-radius:4px}
  .msg.user{justify-content:flex-end}
  .msg.user .b{background:var(--user);color:#fff;border-bottom-right-radius:4px}
  .hint{color:var(--cinza);font-size:13px;text-align:center;margin:6px 0 18px}
  .chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:18px}
  .chip{background:#fff;border:1px solid var(--borda);border-radius:18px;
    padding:8px 14px;font-size:13px;cursor:pointer;color:var(--azul);
    transition:background .15s}
  .chip:hover{background:#e8f1fb}
  footer{border-top:1px solid var(--borda);background:#fff;padding:14px 22px}
  .bar{max-width:820px;margin:0 auto;display:flex;gap:10px}
  textarea{flex:1;resize:none;border:1px solid var(--borda);border-radius:10px;
    padding:12px 14px;font:inherit;font-size:15px;max-height:120px}
  textarea:focus{outline:2px solid var(--verde);border-color:transparent}
  button{background:var(--verde);color:#fff;border:0;border-radius:10px;
    padding:0 22px;font-weight:700;font-size:15px;cursor:pointer}
  button:disabled{opacity:.55;cursor:not-allowed}
  .aviso{max-width:820px;margin:8px auto 0;font-size:11.5px;color:var(--cinza);
    text-align:center}
  .cursor::after{content:"▌";animation:blink 1s steps(1) infinite;color:var(--verde)}
  @keyframes blink{50%{opacity:0}}
</style>
</head>
<body>
<header>
  <h1>Tutor FME</h1>
  <p>Assistente para criar o Fundo Municipal de Esporte — programa O Esporte Que Queremos (PR)</p>
</header>
<main id="chat">
  <div class="hint">Faça uma pergunta simples e eu explico o passo a passo.</div>
  <div class="chips" id="chips">
    <div class="chip">O que é o FME e por que ele importa?</div>
    <div class="chip">Quais são as 5 etapas para criar o Fundo?</div>
    <div class="chip">Quais leis embasam o FME?</div>
    <div class="chip">O que precisa entregar ao programa?</div>
    <div class="chip">Como deve ser a lei do FME?</div>
  </div>
</main>
<footer>
  <div class="bar">
    <textarea id="inp" rows="1" placeholder="Digite sua dúvida sobre o FME..."></textarea>
    <button id="send">Enviar</button>
  </div>
  <div class="aviso">Material de apoio à decisão. Confirme prazos e editais
  vigentes em esporte.pr.gov.br. Não substitui parecer jurídico com OAB.</div>
</footer>
<script>
const chat=document.getElementById('chat');
const inp=document.getElementById('inp');
const send=document.getElementById('send');
const chips=document.getElementById('chips');
const history=[];

function addMsg(role,text){
  const w=document.createElement('div');
  w.className='msg '+(role==='user'?'user':'bot');
  const b=document.createElement('div');
  b.className='b';b.textContent=text;
  w.appendChild(b);chat.appendChild(w);
  chat.scrollTop=chat.scrollHeight;
  return b;
}
chips.addEventListener('click',e=>{
  if(e.target.classList.contains('chip')){inp.value=e.target.textContent;ask();}
});
inp.addEventListener('keydown',e=>{
  if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();ask();}
});
inp.addEventListener('input',()=>{
  inp.style.height='auto';inp.style.height=Math.min(inp.scrollHeight,120)+'px';
});
send.addEventListener('click',ask);

async function ask(){
  const q=inp.value.trim();
  if(!q)return;
  if(chips)chips.style.display='none';
  inp.value='';inp.style.height='auto';
  inp.disabled=send.disabled=true;
  addMsg('user',q);
  history.push({role:'user',content:q});
  const bubble=addMsg('bot','');
  bubble.classList.add('cursor');
  let acc='';
  try{
    const r=await fetch('/api/chat',{
      method:'POST',headers:{'content-type':'application/json'},
      body:JSON.stringify({messages:history})
    });
    const reader=r.body.getReader();
    const dec=new TextDecoder();
    let buf='';
    while(true){
      const {value,done}=await reader.read();
      if(done)break;
      buf+=dec.decode(value,{stream:true});
      const parts=buf.split('\\n\\n');
      buf=parts.pop();
      for(const p of parts){
        const line=p.trim();
        if(!line.startsWith('data:'))continue;
        const data=JSON.parse(line.slice(5).trim());
        if(data.delta){acc+=data.delta;bubble.textContent=acc;
          chat.scrollTop=chat.scrollHeight;}
        if(data.error){acc=data.error;bubble.textContent=acc;}
      }
    }
  }catch(err){
    acc='Erro de conexão. Tente novamente.';bubble.textContent=acc;
  }
  bubble.classList.remove('cursor');
  if(acc)history.push({role:'assistant',content:acc});
  inp.disabled=send.disabled=false;inp.focus();
}
</script>
</body>
</html>`;

# Como subir a campanha no Google Ads Editor — C Marceneiro

Pacote gerado a partir de `campanhagoogleadscmarceneiro.md`. São 7 CSVs
prontos para importação em massa no **Google Ads Editor**.

> Os cabeçalhos dos CSVs estão em inglês de propósito: o Google Ads Editor
> reconhece esses nomes nativamente, mesmo com a interface em português.
> Na tela de importação dá para revisar/ajustar o mapeamento de colunas.

---

## 0. Pré-requisitos

1. Conta no Google Ads já criada, com **fuso e moeda BRL (R$)**.
2. **Google Ads Editor** instalado (gratuito: ads.google.com/editor).
3. Abra o Editor → **Get recent changes / Obter alterações recentes** para
   baixar a conta antes de importar.
4. Tudo é importado como **Pausado** (`Paused`) de propósito — nada vai ao ar
   sem você revisar e ativar.

---

## 1. Ordem de importação (respeite a hierarquia)

Importe **nesta ordem** — grupo depende de campanha, palavra-chave depende de
grupo, etc.:

| Passo | Arquivo | O que cria |
|---|---|---|
| 1 | `01_campanhas.csv` | 3 campanhas Search + 1 Shopping |
| 2 | `02_grupos_de_anuncios.csv` | 10 grupos de anúncio |
| 3 | `03_palavras_chave.csv` | 126 palavras-chave (exata/frase/ampla) + Final URL com UTM |
| 4 | `05_anuncios_rsa.csv` | 1 anúncio responsivo (RSA) por grupo |
| 5 | `04_negativas_por_campanha.csv` | negativas das campanhas Puxadores e MDF |
| 6 | `04_negativas_conta.csv` | lista compartilhada de negativas (conta) |
| 7 | `06_sitelinks.csv` / `07_snippets.csv` | extensões |

### Como importar cada arquivo

**Conta → Importar → De arquivo…** (`Account → Import → From file…`),
selecione o CSV, confira o mapeamento de colunas na pré-visualização e
clique em **Aplicar / Finalizar**. Confira os avisos antes de **Publicar
(Post)**.

> Alternativa para palavras-chave e negativas: tela do nível desejado →
> **Fazer várias alterações (Make multiple changes)** → colar o conteúdo do
> CSV. Útil se a importação por arquivo reclamar de mapeamento.

### Negativas (atenção)

- `04_negativas_por_campanha.csv`: importe normalmente (Campaign + Negative
  Keyword + Match Type) ou cole em **Palavras-chave negativas → nível
  campanha**.
- `04_negativas_conta.csv`: o jeito mais confiável é criar uma **lista de
  negativas compartilhada** (Biblioteca compartilhada → Listas de palavras
  negativas), nome `Negativas C Marceneiro - Conta`, colar as 29 palavras e
  **associar às 3 campanhas Search**.

---

## 2. O que NÃO está no CSV e precisa ser configurado à mão

Estes itens o Editor não importa bem por arquivo — configure no Editor
(ou no Google Ads web) por campanha:

- **Localização**: cidade-sede + regiões metropolitanas atendidas. Se for
  nacional, ajuste de lance: **SP +20%, MG +10%, PR/SC +10%, RJ +5%**.
- **Idioma**: Português.
- **Horário de veiculação**: Seg–Sex 07h–19h, Sáb 07h–13h, Dom pausar (ou
  −50%).
- **Ajuste de dispositivos**: Mobile −20%, Tablet −30%, Desktop padrão.
- **Rede**: Search apenas (desligar parceiros de pesquisa no início).
- **Conversões / Google Tag**: configure no Google Ads **web** (formulário,
  clique no telefone, clique no WhatsApp). Sem isso o lance automático não
  funciona depois.
- **Extensão de chamada / formulário de lead**: adicionar no web.
- **Campanha Shopping**: vem só como "casca" pausada. Exige **Merchant
  Center + feed de produtos** vinculado; os grupos/produtos são criados
  depois do feed aprovado.

---

## 3. Antes de publicar (Post)

- O número de WhatsApp no site ainda é o **placeholder `5511999999999`**
  (em `index.html`). Troque pelo número real antes de gastar verba.
- A landing page é o catálogo single-page (`cmarceneiro.com.br`). Os grupos
  de **MDF** e **Ferragens** apontam para a home — o ideal é ter páginas/
  seções dedicadas para esses produtos antes de escalar.
- Confira o **Checklist Pré-Lançamento** do plano (tag de conversão,
  telefone clicável no mobile, UTM, etc.).
- Revise os avisos amarelos/vermelhos no Editor → **Publicar**.

---

## 4. Trocar o cenário de orçamento

O `01_campanhas.csv` já vem no **cenário Conservador** (plano: começar
conservador na semana 1):

| Campanha | Conservador | Moderado | Agressivo |
|---|---|---|---|
| Search Puxadores | 25 | 60 | 120 |
| Search MDF | 20 | 50 | 100 |
| Search Ferragens | 15 | 40 | 80 |
| Shopping | 0 | 30 | 50 |

Para mudar: edite a coluna `Campaign Daily Budget` no `01_campanhas.csv`
e reimporte, ou ajuste o orçamento direto no Editor.

Estratégia de lance por fase: **Sem. 1–3 CPC manual** (R$ 3,00–4,50) →
**Sem. 4–6 Maximizar Conversões** (após 20+ conv.) → **Mês 2+ CPA/ROAS
desejado**.

---

## 5. Regerar os CSVs

Se editar o plano e quiser regerar tudo:

```bash
cd google-ads-cmarceneiro
python3 gerar_csvs.py
```

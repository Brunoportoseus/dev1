# -*- coding: utf-8 -*-
"""
Gera os arquivos CSV de importacao do Google Ads Editor para o C Marceneiro,
a partir do plano em campanhagoogleadscmarceneiro.md.

Saida: arquivos .csv em UTF-8 com cabecalhos em ingles (reconhecidos
nativamente pelo Google Ads Editor em qualquer idioma de interface).

Para regerar:  python3 gerar_csvs.py
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SITE = "https://cmarceneiro.com.br/"
MAX_CPC = "3.50"          # CPC manual inicial (R$ 3,00-4,50 no plano)
STATUS = "Paused"          # importar pausado por seguranca; ativar na conta

# ---------------------------------------------------------------------------
# 1. CAMPANHAS  (cenario CONSERVADOR como padrao - ver INSTRUCOES.md)
# ---------------------------------------------------------------------------
CAMPANHAS = [
    # nome, slug_utm, tipo, orcamento_diario
    ("CMARCENEIRO | GG | SEARCH | PUXADORES | LEADS",
     "cmarceneiro-search-puxadores-leads", "Search", "25"),
    ("CMARCENEIRO | GG | SEARCH | MDF | LEADS",
     "cmarceneiro-search-mdf-leads", "Search", "20"),
    ("CMARCENEIRO | GG | SEARCH | FERRAGENS | LEADS",
     "cmarceneiro-search-ferragens-leads", "Search", "15"),
    ("CMARCENEIRO | GG | SHOPPING | CATALOGO | VENDAS",
     "cmarceneiro-shopping-catalogo-vendas", "Shopping", "0"),
]
CAMP_SLUG = {c[0]: c[1] for c in CAMPANHAS}

# ---------------------------------------------------------------------------
# 2. GRUPOS DE ANUNCIO + PALAVRAS-CHAVE
#    estrutura: campanha -> { grupo: {"exact":[], "phrase":[], "broad":[]} }
# ---------------------------------------------------------------------------
P = "CMARCENEIRO | GG | SEARCH | PUXADORES | LEADS"
M = "CMARCENEIRO | GG | SEARCH | MDF | LEADS"
F = "CMARCENEIRO | GG | SEARCH | FERRAGENS | LEADS"

ESTRUTURA = {
    P: {
        "PUXADORES | COMPRA | GERAL": {
            "exact": [
                "comprar puxador para movel", "puxador para armario preco",
                "puxador de movel atacado", "puxadores para marcenaria",
                "fornecedor de puxadores",
            ],
            "phrase": [
                "comprar puxadores para moveis",
                "puxadores para marcenaria atacado",
                "puxador para armario onde comprar",
                "loja de puxadores para moveis", "puxador de movel preco",
            ],
            "broad": [
                "puxador movel comprar atacado",
                "puxador marcenaria fornecedor",
                "puxador armario barato quantidade",
            ],
        },
        "PUXADORES | COMPRA | INOX": {
            "exact": [
                "puxador inox para movel", "puxador de inox atacado",
                "puxador inox cozinha preco", "comprar puxador inox",
                "puxador inox escovado",
            ],
            "phrase": [
                "puxador de inox para armario", "puxador inox para marcenaria",
                "puxadores inox onde comprar", "puxador inox escovado preco",
                "puxador inox cozinha atacado", "fornecedor puxador inox",
                "puxador em inox para moveis planejados",
                "puxador inox tubular preco",
            ],
            "broad": [],
        },
        "PUXADORES | COMPRA | ALUMINIO": {
            "exact": [
                "puxador de aluminio para movel", "puxador aluminio atacado",
                "puxador aluminio marcenaria", "comprar puxador aluminio",
                "puxador aluminio preco",
            ],
            "phrase": [
                "puxador de aluminio para armario",
                "puxadores de aluminio onde comprar",
                "puxador aluminio para marcenaria atacado",
                "fornecedor puxador aluminio",
                "puxador aluminio escovado preco", "puxador aluminio cozinha",
                "puxador de aluminio para porta de armario",
            ],
            "broad": [],
        },
        "PUXADORES | COMPRA | ARMARIO-COZINHA": {
            "exact": [
                "puxador para armario de cozinha", "puxador cozinha planejada",
                "puxador movel planejado preco", "puxador para cozinha atacado",
                "puxador para moveis planejados",
            ],
            "phrase": [
                "puxador para armario de cozinha preco",
                "puxadores para moveis planejados atacado",
                "onde comprar puxador para cozinha",
                "puxador para porta de armario cozinha",
                "puxador armario planejado inox aluminio",
                "fornecedor puxador cozinha marceneiro",
                "puxador movel cozinha barato atacado",
            ],
            "broad": [],
        },
    },
    M: {
        "MDF | ORCAMENTO | CHAPAS": {
            "exact": [
                "chapa de mdf preco", "mdf atacado marcenaria",
                "comprar chapa mdf", "fornecedor de mdf",
                "mdf chapa inteira preco",
            ],
            "phrase": [
                "chapa de mdf onde comprar", "preco chapa mdf marcenaria",
                "mdf atacado preco por chapa", "fornecedor mdf para marceneiro",
                "comprar mdf em quantidade", "distribuidor de mdf",
                "mdf chapa 18mm preco", "mdf 15mm chapa inteira atacado",
            ],
            "broad": [],
        },
        "MDF | ORCAMENTO | CRU": {
            "exact": [
                "mdf cru preco", "chapa mdf cru atacado", "mdf cru marcenaria",
                "comprar mdf cru", "mdf cru chapa inteira",
            ],
            "phrase": [
                "mdf cru onde comprar", "preco mdf cru por chapa",
                "mdf cru 18mm preco", "fornecedor mdf cru marceneiro",
                "mdf cru atacado", "chapa mdf cru barata marcenaria",
                "mdf cru distribuidor preco",
            ],
            "broad": [],
        },
        "MDF | ORCAMENTO | REVESTIDO": {
            "exact": [
                "mdf revestido preco", "mdf bp preco", "mdf revestido atacado",
                "mdf melanina preco", "chapa mdf revestido marcenaria",
            ],
            "phrase": [
                "mdf revestido onde comprar", "preco mdf bp marceneiro",
                "mdf revestido branco preco chapa", "mdf bp atacado distribuidor",
                "chapa mdf melanina preco",
                "fornecedor mdf revestido marcenaria",
                "mdf bp 15mm 18mm preco atacado",
            ],
            "broad": [],
        },
    },
    F: {
        "FERRAGENS | COMPRA | DOBRADICAS": {
            "exact": [
                "dobradica para movel preco", "dobradica marcenaria atacado",
                "comprar dobradica para armario", "dobradica para porta de movel",
                "dobradica caneco preco",
            ],
            "phrase": [
                "dobradica para movel onde comprar",
                "dobradica marcenaria preco atacado",
                "fornecedor dobradica para moveis",
                "dobradica caneco 35mm preco", "dobradica oculta para armario",
                "dobradica para porta de armario preco",
                "dobradica hidraulica movel preco",
                "dobradica para marceneiro atacado",
            ],
            "broad": [],
        },
        "FERRAGENS | COMPRA | CORREDICAS": {
            "exact": [
                "corredica para gaveta preco", "corredica telescopica atacado",
                "corredica para movel marcenaria", "comprar corredica gaveta",
                "corredica invisivel preco",
            ],
            "phrase": [
                "corredica para gaveta onde comprar",
                "corredica telescopica preco atacado",
                "fornecedor corredica para marceneiro",
                "corredica gaveta 450mm preco", "corredica com soft close preco",
                "corredica de movel atacado distribuidor",
                "corredica under mount preco marcenaria",
                "corredica para movel planejado atacado",
            ],
            "broad": [],
        },
        "FERRAGENS | COMPRA | MARCENARIA-GERAL": {
            "exact": [
                "ferragens para marcenaria", "ferragens para moveis atacado",
                "fornecedor ferragens marcenaria",
                "ferragens para moveis planejados",
                "acessorios para marcenaria preco",
            ],
            "phrase": [
                "ferragens para marcenaria atacado",
                "loja de ferragens para moveis",
                "ferragens para marceneiro onde comprar",
                "acessorios para moveis planejados atacado",
                "ferragens para armario planejado preco",
                "distribuidor ferragens marcenaria",
                "ferragens moveis preco atacado",
                "suprimentos para marcenaria preco",
            ],
            "broad": [],
        },
    },
}

# ---------------------------------------------------------------------------
# 3. NEGATIVAS
# ---------------------------------------------------------------------------
NEG_CONTA = [
    "diy", "faça voce mesmo", "como fazer", "tutorial", "video aula",
    "curso de marcenaria", "escola de marcenaria", "aprender marcenaria",
    "emprego marceneiro", "vaga marceneiro", "curriculo",
    "trabalho marceneiro", "gratis", "gratuito", "de graca", "segunda mao",
    "usado", "seminovo", "decoracao", "inspiracao", "pinterest",
    "ideias de cozinha",
    # intencao errada (plano: todas as campanhas)
    "conserto", "reparo", "assistencia tecnica", "garantia", "recall",
    "reclamacao", "reclame aqui",
]
NEG_POR_CAMPANHA = {
    P: ["dobradica", "corredica", "mdf", "chapa", "parafuso", "cola",
        "verniz", "lixa"],
    M: ["puxador", "dobradica", "corredica", "madeira macica",
        "compensado", "osb"],
}

# ---------------------------------------------------------------------------
# 4. RSA - 15 headlines + 4 descricoes por campanha (do plano)
# ---------------------------------------------------------------------------
RSA = {
    P: {
        "paths": ("puxadores", "atacado"),
        "h": [
            "Puxadores para Marcenaria", "Atacado de Puxadores SP",
            "Puxador Inox e Aluminio", "Entrega para Todo Brasil",
            "Minimo de Pecas Reduzido", "Faca seu Orcamento Agora",
            "Puxadores com Preco Fabrica", "Marceneiros Atendemos Diario",
            "Puxador Cozinha e Armario", "Catalogo com +500 Modelos",
            "Puxador Tubular e Concha", "Preco Especial no Atacado",
            "Ligue e Garanta seu Pedido", "Fornecedor Direto de Fabrica",
            "Puxadores Entrega Rapida",
        ],
        "d": [
            "Puxadores em inox, aluminio e zamak para moveis planejados e marcenaria. Atacado.",
            "Fornecimento para marceneiros e moveleiros. Estoque disponivel. Orcamento em minutos.",
            "Centenas de modelos de puxadores com preco competitivo. Faca seu pedido hoje mesmo.",
            "Atendimento direto ao marceneiro. Minimo acessivel. Entrega rapida. Fale conosco.",
        ],
    },
    M: {
        "paths": ("mdf", "atacado"),
        "h": [
            "Chapa de MDF Atacado", "MDF Cru e Revestido SP",
            "Fornecedor de MDF Direto", "MDF 15mm e 18mm Estoque",
            "Chapas de MDF por Carga", "Orcamento de MDF Rapido",
            "Distribuidor MDF Marcenaria", "MDF BP Preco de Atacado",
            "Entrega de Chapas MDF", "MDF Melanina e Cru",
            "Pedido Minimo Flexivel", "Preco por Chapa Inteira",
            "MDF com Nota Fiscal", "Retirada ou Entrega MDF",
            "Fale com Nosso Consultor",
        ],
        "d": [
            "Chapas de MDF cru e revestido para marceneiros e moveleiros. Preco de distribuidor.",
            "Fornecimento de MDF em quantidade para marcenaria. Estoque amplo. Orcamento hoje.",
            "MDF 15mm, 18mm, BP e melanina com entrega ou retirada. Atendemos todo o estado.",
            "Distribuidora de MDF com preco justo e pedido minimo acessivel. Fale agora conosco.",
        ],
    },
    F: {
        "paths": ("ferragens", "atacado"),
        "h": [
            "Ferragens para Marcenaria", "Dobradicas e Corredicas SP",
            "Ferragens para Movel Atacado", "Corredica Soft Close Preco",
            "Dobradica Caneco Atacado", "Acessorios para Marceneiro",
            "Ferragens para Planejados", "Estoque de Ferragens Amplo",
            "Orcamento de Ferragens", "Fornecedor Ferragens Direto",
            "Dobradica Hidraulica Preco", "Corredica Telescopica Stock",
            "Entrega Rapida de Ferragens", "Preco Especial para Lojistas",
            "Fale com Especialista Agora",
        ],
        "d": [
            "Dobradicas, corredicas, puxadores e acessorios para marcenaria. Preco de atacado.",
            "Ferragens para moveis planejados com estoque disponivel. Atendemos marceneiros e lojistas.",
            "Corredicas com soft close, dobradicas hidraulicas e muito mais. Orcamento sem compromisso.",
            "Fornecedora de ferragens para marcenaria com entrega em todo o estado. Faca seu pedido.",
        ],
    },
}

# ---------------------------------------------------------------------------
# 5. SITELINKS + SNIPPETS
# ---------------------------------------------------------------------------
SITELINKS = {
    P: [
        ("Puxadores de Inox", "Modelos escovados e polidos", "Atacado para marceneiros"),
        ("Puxadores de Aluminio", "Tubular e perfil", "Varios tamanhos em estoque"),
        ("Faca seu Orcamento", "Resposta em ate 1 hora", "Sem compromisso"),
        ("Fale pelo WhatsApp", "Atendimento imediato", "Tire suas duvidas agora"),
    ],
    M: [
        ("MDF Cru", "Chapas 15mm e 18mm", "Preco de distribuidor"),
        ("MDF Revestido (BP)", "Melanina e formica", "Varios acabamentos"),
        ("Tabela de Precos", "Precos atualizados", "Validos para atacado"),
        ("Solicitar Orcamento", "Rapido e sem burocracia", "Respondemos rapido"),
    ],
    F: [
        ("Dobradicas", "Caneco, hidraulica, oculta", "Estoque disponivel"),
        ("Corredicas", "Telescopica e soft close", "Varios tamanhos"),
        ("Catalogo Completo", "Todos os produtos", "Ferragens para marcenaria"),
        ("Fale com Consultor", "Atendimento especializado", "Resposta rapida"),
    ],
}
SNIPPETS = {
    P: ("Tipos", ["Inox", "Aluminio", "Zamak", "Tubular", "Concha", "Perfil", "Colonial"]),
    M: ("Tipos", ["MDF Cru", "MDF BP", "MDF Melanina", "15mm", "18mm", "Revestido"]),
    F: ("Tipos", ["Dobradicas", "Corredicas", "Parafusos", "Suportes", "Fechaduras", "Soft Close"]),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def slug(texto):
    return (texto.lower().replace(" | ", "-").replace(" ", "-")
            .replace("|", "-"))


def final_url(campanha, grupo):
    return (f"{SITE}?utm_source=google&utm_medium=cpc"
            f"&utm_campaign={CAMP_SLUG[campanha]}"
            f"&utm_content={slug(grupo)}&utm_term={{keyword}}")


def write_csv(nome, header, rows):
    caminho = os.path.join(BASE_DIR, nome)
    with open(caminho, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"  {nome}: {len(rows)} linhas")


# ---------------------------------------------------------------------------
# Geracao
# ---------------------------------------------------------------------------
def main():
    print("Gerando CSVs do Google Ads Editor...")

    # 01 - Campanhas
    rows = []
    for nome, _slugv, tipo, orc in CAMPANHAS:
        rows.append([nome, tipo, STATUS, orc, "Manual CPC"])
    write_csv("01_campanhas.csv",
              ["Campaign", "Campaign Type", "Status",
               "Campaign Daily Budget", "Bid Strategy Type"], rows)

    # 02 - Grupos de anuncio
    rows = []
    for camp, grupos in ESTRUTURA.items():
        for grupo in grupos:
            rows.append([camp, grupo, STATUS, MAX_CPC])
    write_csv("02_grupos_de_anuncios.csv",
              ["Campaign", "Ad Group", "Status", "Max CPC"], rows)

    # 03 - Palavras-chave
    rows = []
    for camp, grupos in ESTRUTURA.items():
        for grupo, kws in grupos.items():
            url = final_url(camp, grupo)
            for mt, lista in (("Exact", kws["exact"]),
                              ("Phrase", kws["phrase"]),
                              ("Broad", kws["broad"])):
                for kw in lista:
                    rows.append([camp, grupo, kw, mt, STATUS, url])
    write_csv("03_palavras_chave.csv",
              ["Campaign", "Ad Group", "Keyword", "Match Type",
               "Status", "Final URL"], rows)

    # 04a - Negativas de conta (lista compartilhada)
    rows = [["Negativas C Marceneiro - Conta", kw, "Phrase"]
            for kw in NEG_CONTA]
    write_csv("04_negativas_conta.csv",
              ["Negative Keyword List", "Keyword", "Match Type"], rows)

    # 04b - Negativas por campanha
    rows = []
    for camp, lista in NEG_POR_CAMPANHA.items():
        for kw in lista:
            rows.append([camp, kw, "Phrase"])
    write_csv("04_negativas_por_campanha.csv",
              ["Campaign", "Negative Keyword", "Match Type"], rows)

    # 05 - RSA (1 por grupo, reaproveitando o RSA da campanha)
    hdr = (["Campaign", "Ad Group", "Status"]
           + [f"Headline {i}" for i in range(1, 16)]
           + [f"Description {i}" for i in range(1, 5)]
           + ["Path 1", "Path 2", "Final URL"])
    rows = []
    for camp, grupos in ESTRUTURA.items():
        rsa = RSA[camp]
        for grupo in grupos:
            row = [camp, grupo, STATUS] + rsa["h"] + rsa["d"]
            row += [rsa["paths"][0], rsa["paths"][1], final_url(camp, grupo)]
            rows.append(row)
    write_csv("05_anuncios_rsa.csv", hdr, rows)

    # 06 - Sitelinks
    rows = []
    for camp, sls in SITELINKS.items():
        for texto, d1, d2 in sls:
            rows.append([camp, texto, d1, d2, SITE])
    write_csv("06_sitelinks.csv",
              ["Campaign", "Link Text", "Description 1",
               "Description 2", "Final URL"], rows)

    # 07 - Snippets estruturados
    rows = []
    for camp, (header, valores) in SNIPPETS.items():
        rows.append([camp, header, "; ".join(valores)])
    write_csv("07_snippets.csv",
              ["Campaign", "Header", "Values"], rows)

    # ---- ARQUIVO COMBINADO: campanhas + grupos + KWs + RSAs + neg/camp ----
    hdr = ["Campaign", "Campaign Type", "Campaign Daily Budget",
           "Bid Strategy Type", "Ad Group", "Max CPC",
           "Keyword", "Negative Keyword", "Match Type"]
    hdr += [f"Headline {i}" for i in range(1, 16)]
    hdr += [f"Description {i}" for i in range(1, 5)]
    hdr += ["Path 1", "Path 2", "Final URL", "Status"]

    def empty():
        return [""] * len(hdr)

    idx = {name: i for i, name in enumerate(hdr)}

    def row(**kv):
        r = empty()
        for k, v in kv.items():
            r[idx[k]] = v
        return r

    combined = []

    # 1. Campanhas
    for nome, _slugv, tipo, orc in CAMPANHAS:
        combined.append(row(**{
            "Campaign": nome, "Campaign Type": tipo,
            "Campaign Daily Budget": orc,
            "Bid Strategy Type": "Manual CPC", "Status": STATUS,
        }))

    # 2. Grupos de anuncio
    for camp, grupos in ESTRUTURA.items():
        for grupo in grupos:
            combined.append(row(**{
                "Campaign": camp, "Ad Group": grupo,
                "Max CPC": MAX_CPC, "Status": STATUS,
            }))

    # 3. Palavras-chave
    for camp, grupos in ESTRUTURA.items():
        for grupo, kws in grupos.items():
            url = final_url(camp, grupo)
            for mt, lista in (("Exact", kws["exact"]),
                              ("Phrase", kws["phrase"]),
                              ("Broad", kws["broad"])):
                for kw in lista:
                    combined.append(row(**{
                        "Campaign": camp, "Ad Group": grupo,
                        "Keyword": kw, "Match Type": mt,
                        "Final URL": url, "Status": STATUS,
                    }))

    # 4. RSAs
    for camp, grupos in ESTRUTURA.items():
        rsa = RSA[camp]
        for grupo in grupos:
            kv = {"Campaign": camp, "Ad Group": grupo, "Status": STATUS,
                  "Path 1": rsa["paths"][0], "Path 2": rsa["paths"][1],
                  "Final URL": final_url(camp, grupo)}
            for i, h in enumerate(rsa["h"], 1):
                kv[f"Headline {i}"] = h
            for i, d in enumerate(rsa["d"], 1):
                kv[f"Description {i}"] = d
            combined.append(row(**kv))

    # 5. Negativas por campanha
    for camp, lista in NEG_POR_CAMPANHA.items():
        for kw in lista:
            combined.append(row(**{
                "Campaign": camp, "Negative Keyword": kw,
                "Match Type": "Phrase",
            }))

    write_csv("tudo_em_um.csv", hdr, combined)

    print("Concluido.")


if __name__ == "__main__":
    main()

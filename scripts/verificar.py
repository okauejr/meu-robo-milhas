"""Verificação estrutural do HTML do dia (Passo 6 das REGRAS).

Uso: python scripts/verificar.py relatorios/AAAA-MM-DD.html
Sai com código 1 e lista os problemas se algo estiver errado.
"""
import re
import sys
import unicodedata
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

# Frases que nunca podem aparecer dentro de uma mensagem pro grupo (só no rodapé).
FRASES_BANIDAS = [
    r"\bbug", "erro no site", "erro na pagina", "nao foi possivel", "nao consegui",
    "regulamento", "link quebrado", "quebrado", "taxa padrao", "taxa normal",
    "dia normal", "dias normais", "normalmente", "inconsistente", "divergen",
    "esfera", "compare ?mania", "sem login", "ticker", "carrossel",
]
RESTOS_DE_MODELO = ["{{", "}}", "NOME DA LOJA", "DD/MM", "X pts", "https://..."]
LIMITE_TELEGRAM = 4096


def sem_acento(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto.lower()) if unicodedata.category(c) != "Mn")


class Extrator(HTMLParser):
    """Coleta o texto de cada div.msg-preview e conta tags de abertura/fechamento."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.abre, self.fecha = {}, {}
        self.mensagens, self._prof, self._buf = [], 0, None
        self.tem_rodape = False

    def handle_starttag(self, tag, attrs):
        self.abre[tag] = self.abre.get(tag, 0) + 1
        classes = (dict(attrs).get("class") or "").split()
        if tag == "footer" and "note" in classes:
            self.tem_rodape = True
        if self._buf is not None:
            if tag == "br":
                self._buf.append("\n")
            elif tag == "div":
                self._prof += 1
        elif tag == "div" and "msg-preview" in classes:
            self._buf, self._prof = [], 0

    def handle_endtag(self, tag):
        self.fecha[tag] = self.fecha.get(tag, 0) + 1
        if self._buf is not None and tag == "div":
            if self._prof == 0:
                self.mensagens.append("".join(self._buf).strip())
                self._buf = None
            else:
                self._prof -= 1

    def handle_data(self, data):
        if self._buf is not None:
            self._buf.append(data)


def extrair(html):
    p = Extrator()
    p.feed(html)
    return p


def verificar(caminho):
    html = Path(caminho).read_text(encoding="utf-8")
    p = extrair(html)
    erros = []

    for tag in ("article", "details", "footer", "main"):
        if p.abre.get(tag, 0) != p.fecha.get(tag, 0):
            erros.append(f"<{tag}> abre {p.abre.get(tag, 0)}x e fecha {p.fecha.get(tag, 0)}x")
    if not p.tem_rodape:
        erros.append('faltou o rodapé <footer class="note">')
    if p.abre.get("article", 0) != len(p.mensagens):
        erros.append(f"{p.abre.get('article', 0)} cards mas {len(p.mensagens)} mensagens (msg-preview)")
    if html.count('class="copiar"') != len(p.mensagens):
        erros.append("cada mensagem precisa de um botão Copiar")

    for resto in RESTOS_DE_MODELO:
        if resto in html:
            erros.append(f"sobrou texto do modelo: {resto!r}")

    data = re.search(r"(\d{4})-(\d{2})-(\d{2})", Path(caminho).name)
    if data:
        dia = datetime(*map(int, data.groups()))
        if dia.strftime("%d/%m/%Y") not in html:
            erros.append(f"a data {dia:%d/%m/%Y} não aparece no arquivo (cabeçalho desatualizado?)")

    for i, msg in enumerate(p.mensagens, 1):
        normal = sem_acento(msg)
        for frase in FRASES_BANIDAS:
            if re.search(frase, normal):
                erros.append(f"mensagem #{i} contém frase banida: {frase!r}")
        if len(msg) > LIMITE_TELEGRAM:
            erros.append(f"mensagem #{i} tem {len(msg)} caracteres (limite do Telegram {LIMITE_TELEGRAM})")
        if not msg.startswith("*"):
            erros.append(f"mensagem #{i} deveria começar com o título em negrito (*...*)")

    return erros, p


if __name__ == "__main__":
    erros, p = verificar(sys.argv[1])
    if erros:
        print("PROBLEMAS:")
        for e in erros:
            print(" -", e)
        sys.exit(1)
    print(f"OK: {len(p.mensagens)} card(s), estrutura e mensagens limpas.")

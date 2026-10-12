"""Procura posts de hoje sobre o "Meu Resgate Favorito" da Azul Fidelidade.

Os sites da Azul bloqueiam acesso vindo da nuvem, então a checagem das 15h usa
os sites de milhas que publicam a oferta poucos minutos depois de ela abrir
(Passageiro de Primeira pelo feed RSS, Pontos pra Voar pela busca do site).

Uso: python scripts/azul_resgate.py [--data AAAA-MM-DD]
Imprime um post por linha: "horário | fonte | título | link". Sem nada hoje,
imprime "NADA".
"""
import argparse
import html
import re
import sys
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

import requests

BRT = timezone(timedelta(hours=-3))
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")
FEED_PP = "https://passageirodeprimeira.com/?s=resgate+favorito&feed=rss2"
BUSCA_PPV = "https://pontospravoar.com/?s=resgate+favorito"
FILTRO = re.compile(r"resgate favorito", re.I)


def passageiro_de_primeira():
    r = requests.get(FEED_PP, headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    for item in re.findall(r"<item>(.*?)</item>", r.text, re.S):
        titulo = html.unescape(re.search(r"<title>(.*?)</title>", item, re.S).group(1))
        link = re.search(r"<link>(.*?)</link>", item, re.S).group(1).strip()
        quando = parsedate_to_datetime(re.search(r"<pubDate>(.*?)</pubDate>", item).group(1))
        yield quando.astimezone(BRT), "Passageiro de Primeira", titulo, link


def pontos_pra_voar():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(user_agent=UA, locale="pt-BR")
        pg.goto(BUSCA_PPV, wait_until="domcontentloaded", timeout=90000)
        posts = pg.evaluate("""() => [...document.querySelectorAll('time[datetime]')].map(t => {
            let c = t.parentElement;
            while (c && !c.querySelector('h2 a, h3 a')) c = c.parentElement;
            const a = c && c.querySelector('h2 a, h3 a');
            return a ? [t.getAttribute('datetime'), a.innerText.trim(), a.href] : null;
        }).filter(Boolean)""")
        b.close()
    for quando, titulo, link in posts:
        yield datetime.fromisoformat(quando).astimezone(BRT), "Pontos pra Voar", titulo, link


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--data", help="dia a procurar (padrão: hoje em Brasília)")
    dia = a.parse_args().data or datetime.now(BRT).strftime("%Y-%m-%d")

    achados, vistos = [], set()
    for fonte in (passageiro_de_primeira, pontos_pra_voar):
        try:
            for quando, nome, titulo, link in fonte():
                if quando.strftime("%Y-%m-%d") == dia and FILTRO.search(titulo) and link not in vistos:
                    vistos.add(link)
                    achados.append(f"{quando:%H:%M} | {nome} | {titulo} | {link}")
        except Exception as e:  # uma fonte fora do ar não derruba a outra
            print(f"AVISO: {fonte.__name__} falhou: {e}", file=sys.stderr)
    print("\n".join(sorted(achados)) if achados else "NADA")


if __name__ == "__main__":
    main()

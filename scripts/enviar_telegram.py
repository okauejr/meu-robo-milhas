"""Envia o HTML do dia pro Telegram (Passo 7 das REGRAS).

Manda o arquivo como documento e, em seguida, cada mensagem do grupo como
uma mensagem de texto separada (texto puro, pra copiar e colar no WhatsApp
com os *negritos* intactos).

Uso:
  python scripts/enviar_telegram.py relatorios/AAAA-MM-DD.html [--legenda "texto"]
  python scripts/enviar_telegram.py --texto "mensagem avulsa"

Precisa das variáveis de ambiente TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID.
"""
import argparse
import os
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from verificar import verificar  # noqa: E402

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT = os.environ.get("TELEGRAM_CHAT_ID")


def chamar(metodo, dados, arquivos=None):
    url = f"https://api.telegram.org/bot{TOKEN}/{metodo}"
    for _ in range(5):
        r = requests.post(url, data=dados, files=arquivos, timeout=60)
        corpo = r.json()
        if corpo.get("ok"):
            return corpo
        espera = corpo.get("parameters", {}).get("retry_after")
        if not espera:
            raise SystemExit(f"Telegram recusou {metodo}: {corpo.get('description')}")
        time.sleep(espera + 1)
    raise SystemExit(f"Telegram: muitas tentativas em {metodo}")


def texto(msg):
    chamar("sendMessage", {"chat_id": CHAT, "text": msg, "disable_web_page_preview": "true"})


def main():
    a = argparse.ArgumentParser()
    a.add_argument("html", nargs="?")
    a.add_argument("--legenda", default="")
    a.add_argument("--texto")
    args = a.parse_args()
    if not TOKEN or not CHAT:
        raise SystemExit("Defina TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID nas variáveis do ambiente.")

    if args.texto:
        texto(args.texto)
        return

    erros, p = verificar(args.html)
    if erros:
        raise SystemExit("Não enviei: o HTML não passou na verificação.\n - " + "\n - ".join(erros))

    caminho = Path(args.html)
    n = len(p.mensagens)
    legenda = args.legenda or (f"{n} oportunidade(s) nova(s) hoje" if n else "Nenhuma oportunidade nova começando hoje")
    with caminho.open("rb") as f:
        chamar("sendDocument", {"chat_id": CHAT, "caption": legenda[:1024]},
               {"document": (caminho.name, f, "text/html")})
    for msg in p.mensagens:
        time.sleep(1)
        texto(msg)
    print(f"Enviado: arquivo + {n} mensagem(ns).")


if __name__ == "__main__":
    main()

"""Envia as mensagens do dia pro Telegram (Passo 7 das REGRAS).

Manda cada mensagem do grupo (os blocos msg-preview do HTML do dia) como uma
mensagem de texto separada, em texto puro, pra copiar e colar no WhatsApp com
os *negritos* intactos. O arquivo HTML em si não é enviado. Sem nenhuma
oportunidade, manda só um aviso curto.

Uso:
  python scripts/enviar_telegram.py relatorios/AAAA-MM-DD.html
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

    if not p.mensagens:
        texto("Nenhuma oportunidade nova começando hoje.")
    for i, msg in enumerate(p.mensagens):
        if i:
            time.sleep(1)
        texto(msg)
    print(f"Enviado: {len(p.mensagens)} mensagem(ns).")


if __name__ == "__main__":
    main()

"""Envia as mensagens do dia pro Telegram (Passo 7 das REGRAS).

Manda cada mensagem do grupo (os blocos msg-preview do HTML do dia) como uma
mensagem de texto separada, em texto puro, pra copiar e colar no WhatsApp com
os *negritos* intactos. Se o card tiver banner (<img class="banner">), a foto
vai logo antes da mensagem. O arquivo HTML em si não é enviado. Sem nenhuma
oportunidade, manda só um aviso curto (ou nada, com --silencioso).

Mensagens já enviadas ficam registradas em relatorios/AAAA-MM-DD.enviados.json
e nunca são reenviadas, então dá pra rodar de novo no mesmo dia (checagens
extras das 18h, correções) sem duplicar nada no Telegram.

Uso:
  python scripts/enviar_telegram.py relatorios/AAAA-MM-DD.html [--silencioso]
  python scripts/enviar_telegram.py --texto "mensagem avulsa"

Precisa das variáveis de ambiente TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID.
"""
import argparse
import hashlib
import json
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


def foto(caminho):
    with open(caminho, "rb") as f:
        chamar("sendPhoto", {"chat_id": CHAT}, {"photo": (Path(caminho).name, f)})


def main():
    a = argparse.ArgumentParser()
    a.add_argument("html", nargs="?")
    a.add_argument("--texto")
    a.add_argument("--foto", help="com --texto: manda essa imagem antes do texto")
    a.add_argument("--silencioso", action="store_true",
                   help="sem mensagem nova, não manda nada (checagens extras)")
    args = a.parse_args()
    if not TOKEN or not CHAT:
        raise SystemExit("Defina TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID nas variáveis do ambiente.")

    if args.texto:
        if args.foto:
            foto(args.foto)
        texto(args.texto)
        return

    erros, p = verificar(args.html)
    if erros:
        raise SystemExit("Não enviei: o HTML não passou na verificação.\n - " + "\n - ".join(erros))

    registro = Path(args.html).with_suffix(".enviados.json")
    enviados = json.loads(registro.read_text(encoding="utf-8")) if registro.exists() else []
    pasta = Path(args.html).parent
    novas = [(m, img) for m, img in zip(p.mensagens, p.imagens)
             if hashlib.sha1(m.encode()).hexdigest() not in enviados]

    if not novas:
        if not args.silencioso and not enviados:
            texto("Nenhuma oportunidade nova começando hoje.")
            enviados.append("aviso-nada")
            registro.write_text(json.dumps(enviados, indent=1), encoding="utf-8")
        print("Nada novo para enviar.")
        return
    for i, (msg, img) in enumerate(novas):
        if i:
            time.sleep(1)
        if img:
            foto(pasta / img)
        texto(msg)
        enviados.append(hashlib.sha1(msg.encode()).hexdigest())
        registro.write_text(json.dumps(enviados, indent=1), encoding="utf-8")
    print(f"Enviado: {len(novas)} mensagem(ns) nova(s).")

if __name__ == "__main__":
    main()

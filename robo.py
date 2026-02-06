import requests
import os
import telegram
from telegram import constants
import asyncio
from datetime import datetime

# --- CONFIGURAÇÕES ---
SEATS_AERO_API_KEY = 'pro_2bJs2oDe5Y38YGwrqHDAXqLHb6T'
TELEGRAM_BOT_TOKEN = '8403298714:AAEWbqrbo7ARo_DQlOTFqBFchySUxzBRTfQ'
TELEGRAM_CHAT_ID = '1072884350'

LIMIT_ECONOMY_NATIONAL = 30000
LIMIT_ECONOMY_INTERNATIONAL = 70000
LIMIT_BUSINESS = 200000

BRAZIL_AIRPORTS = ['GRU', 'GIG', 'BSB', 'VCP', 'CNF', 'POA', 'FOR', 'CWB', 'REC', 'SSA']
MONTHS_PT = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

async def send_telegram_message(message):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode=constants.ParseMode.HTML, disable_web_page_preview=True)
    except Exception as e: print(f"Erro Telegram: {e}")

def format_dates(dates):
    parsed = sorted([datetime.strptime(d, '%Y-%m-%d') for d in dates])
    grouped = {}
    curr_yr = datetime.now().year
    for d in parsed:
        key = (d.month, d.year)
        if key not in grouped: grouped[key] = []
        grouped[key].append(str(d.day))
    out = []
    for (m, y), days in grouped.items():
        name = MONTHS_PT.get(m, str(m))
        yr = f" {y}" if y > curr_yr else ""
        out.append(f"{name}{yr}:\n{', '.join(days)}")
    return '\n'.join(out)

async def main():
    url = "https://api.seats.aero/v1/cached?origin=GRU"
    headers = {'x-api-key': SEATS_AERO_API_KEY}
    try:
        res = requests.get(url, headers=headers, timeout=30 )
        data = res.json().get('data', [])
        for f in data:
            points = int(f.get('YQPoints', 0))
            cabin = f.get('Route', {}).get('Cabin', '').lower()
            dest = f.get('Route', {}).get('DestinationAirport')
            
            match = False
            if cabin == 'business' and points <= LIMIT_BUSINESS: match = True
            elif cabin == 'economy':
                if dest in BRAZIL_AIRPORTS and points <= LIMIT_ECONOMY_NATIONAL: match = True
                elif dest not in BRAZIL_AIRPORTS and points <= LIMIT_ECONOMY_INTERNATIONAL: match = True
            
            if match:
                msg = (f"<b>OPORTUNIDADE DE EMISSÃO</b>\n\n"
                       f"GRU ✈️ {dest}\n"
                       f"<b>Programa:</b> {f.get('Route', {}).get('Source').upper()}\n"
                       f"<b>Classe:</b> {cabin.capitalize()}\n"
                       f"<b>Companhia:</b> {f.get('Route', {}).get('Airlines')}\n\n"
                       f"💺 <b>Valor:</b> {points:,} milhas\n"
                       f"📅 <b>Datas:</b>\n{format_dates([f.get('Date')])}\n⸻\n"
                       f"https://pay.kiwify.com.br/x7e8NzE" )
                await send_telegram_message(msg)
                await asyncio.sleep(2)
    except Exception as e: print(f"Erro: {e}")

if __name__ == '__main__': asyncio.run(main())

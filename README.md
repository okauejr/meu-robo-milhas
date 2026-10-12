# Robô de oportunidades Livelo

Rotina diária (dias úteis) que roda na nuvem do Claude Code, sem precisar de PC
ligado: confere no navegador as oportunidades de pontuação Livelo que **começam
hoje** (Clube Livelo + parceiros), monta um HTML com mensagens prontas pro grupo
de WhatsApp e envia tudo pro Telegram.

- `REGRAS.md` — o passo a passo completo que a rotina segue
- `historico.md` — tudo que já foi enviado (anti-duplicata)
- `relatorios/` — um HTML por dia
- `modelo/dia.html` — modelo do HTML
- `scripts/navegar.py` — navegação com Chromium (texto, links, carrossel, PDF)
- `scripts/verificar.py` — verificação estrutural e de frases banidas
- `scripts/enviar_telegram.py` — envia o arquivo e cada mensagem separada

## Configuração do ambiente na nuvem

1. **Rede** (Network access → Allowed domains): `livelo.com.br`,
   `esfera.com.vc`, `comparemania.com.br`, `api.telegram.org`, mantendo
   *Allow package managers* marcado.
2. **Variáveis de ambiente**: `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID`.

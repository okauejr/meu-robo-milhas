# Rotina diária "Pega as oportunidades de hoje" — Clube Livelo + parceiros

Este é o documento de regras da rotina. A rotina agendada lê este arquivo inteiro
antes de começar. Correções de método (falhas sistemáticas descobertas depois de
um envio) são registradas na seção **Correções de método** no fim deste arquivo.

## Objetivo

Todo dia útil, montar um arquivo HTML único com as oportunidades NOVAS de
pontuação Livelo (campanhas de Clube Livelo e ofertas de parceiros/lojas) cujo
período de validade **começa naquele dia específico**, verificadas diretamente
no navegador (não por busca/texto), e preparar mensagens prontas para copiar e
colar no grupo de WhatsApp. O resultado é enviado pro Telegram.

## Fontes consultadas

- livelo.com.br/juntar-pontos/todos-os-parceiros — filtro "Ofertas", ordenado por "Maior pontuação"
- livelo.com.br/regulamentos-ativos — campanhas de Clube Livelo (adesão, upgrade, compra de pontos)
- esfera.com.vc/junte-pontos/junte-pontos/esf02163 — busca por nome da loja
- comparemania.com.br — ticker da home com lojas em variação verde, usado como triagem adicional (não é fonte primária, pode trazer dado desatualizado)
- O carrossel de banners em destaque no topo da própria página de parceiros da Livelo
- `historico.md` deste repositório — tudo que já foi enviado em dias anteriores (loja/taxa/período), usado pra nunca reenviar a mesma oportunidade

## Passo 1 — Checagem do Clube Livelo (sempre, mesmo sem novidade)

Entrar em livelo.com.br/regulamentos-ativos e procurar campanhas de adesão,
upgrade ou compra de pontos com desconto cujo Período COMEÇA no dia de hoje
(não qualquer uma ainda rodando). Ler o regulamento completo em PDF até o fim
(tabela de bônus inteira + cláusulas de elegibilidade, que geralmente vêm depois
da tabela).

- Só consolidar adesão e upgrade no mesmo card quando os dois regulamentos
  cobrem exatamente o mesmo plano, pontuação e público — qualquer diferença de
  escopo vira mensagem separada.
- Preço: valor de vitrine sem login (modal "Escolha o tipo de assinatura" em
  livelo.com.br/clube: mensal, anual parcelado em 12x, anual à vista).
- Preço do milheiro de cada modalidade = total pago em 12 meses ÷ total de
  pontos em 12 meses daquela modalidade específica (× 1000) — nunca presumir
  taxa simétrica entre modalidades.
- Cupom + desconto por forma de pagamento (ex. Pix): aplicar em cascata
  (multiplicando), nunca somando os percentuais.

## Passo 2 — Levantamento de candidatas de parceiro

Quatro canais, todos obrigatórios e no mesmo nível de prioridade:

1. Filtro Ofertas/Maior pontuação da própria Livelo
2. Busca por loja na Esfera
3. Ticker principal do Compare Mania (lojas com variação verde na home)
4. Carrossel de banners em destaque no topo da página de parceiros da Livelo —
   percorrer TODOS os slides clicando repetidamente na seta de avançar (que fica
   abaixo da imagem — nunca clicar na própria imagem, que é um link pra página do
   parceiro) até o carrossel repetir o primeiro slide. O número de bolinhas
   indicadoras não é confiável como contagem. (`scripts/navegar.py carrossel` faz isso.)

## Passo 3 — Verificação individual de cada candidata

Pra cada loja levantada por qualquer um dos 4 canais, entrar na página específica
do parceiro (não só no card da listagem) nas DUAS plataformas (Livelo e Esfera) e
confirmar: a régua completa de pontos por tier (assinante Clube / sem Clube /
categoria restrita), a validade exata ("Campanha válida de X a Y" ou "Campanha
válida em DD/MM", geralmente no rodapé da página ou do banner) e as restrições
(cupom, categoria de produto, prazo de crédito). Só incluir se houver bônus
REALMENTE ativo (badge de promoção, contador de validade, cupom) — nunca a taxa
padrão do dia a dia.

**Critério de inclusão:** o período da campanha precisa COMEÇAR hoje, não só
estar "ainda rodando". Uma campanha que começou dias atrás e só termina hoje fica
de fora (ela já deveria ter entrado no dia em que começou).

**Critério de desempate** quando a página do parceiro tem texto de data
inconsistente ou com bug de formatação. Três sinais; qualquer um sozinho já pode
confirmar, mas o ideal é bater mais de um:

- (a) o contador "Termina em X horas/dias" da própria página — se indica término
  ainda hoje, é campanha de hoje;
- (b) variação em verde no ticker do Compare Mania pra aquela loja;
- (c) o texto de validade do banner do carrossel, quando limpo e sem ambiguidade —
  tratado como a fonte mais confiável quando bate com um texto bugado na página
  individual do parceiro.

**Fora sempre:** produtos de nicho (seguros de viagem, consórcios, planos de saúde
pet, aluguel de carro restrito a um país), mesmo com bônus real; campanhas
fechadas por convite.

## Passo 4 — Checagem de novidade (anti-duplicata)

Comparar cada candidata aprovada contra `historico.md`. Só conta como "nova" se
mudou a taxa de pontos ou a janela de validade em relação ao que já foi enviado —
a mesma campanha recorrente só com data atualizada não é reenviada.

## Passo 5 — Montagem do arquivo HTML

Um arquivo único por dia em `relatorios/AAAA-MM-DD.html` (nunca separado por
categoria), partindo de `modelo/dia.html`, com:

- cabeçalho (data DD/MM/AAAA + fontes);
- um `<article class="card">` por oportunidade: numeração, badge de como foi
  conferido, badge de validade, título, número grande de pontos, grade de fatos,
  um `<details>` com a mensagem pronta (`<div class="msg-preview">`) e o botão
  "Copiar mensagem";
- rodapé `<footer class="note">` só pra uso interno: o que foi checado, o que
  ficou de fora e por quê, e qualquer problema/bug de site encontrado.

Sem nenhuma oportunidade nova, o arquivo sai mesmo assim, com
`<p class="nada">Nenhuma oportunidade nova começando hoje.</p>` e o rodapé
explicando o que foi checado.

**Regra mais importante de formatação:** a mensagem do grupo (dentro de
`msg-preview`) NUNCA pode conter explicação de dificuldade do processo de
verificação — bug do site, link quebrado, "não foi possível confirmar X",
comparação com a outra plataforma, menção à taxa padrão de dias normais. Isso só
passa insegurança sobre uma oportunidade real. Esse tipo de nota fica só no
rodapé. Dentro do card, no máximo uma frase curta e neutra tipo "Preço de
vitrine (sem cupom)", sem explicar o motivo.

### Template de mensagem de parceiro

Título e nome de cupom em negrito (asteriscos do WhatsApp), linha em branco entre seções:

```
*NOME DA LOJA: BENEFÍCIO*

📈 Bonificação
· detalhes dos pontos por tier

📅 Validade
· datas

⚠️ Importante
· cupom, limites, prazo de crédito

🔗 Acesse:
link direto
```

### Template de Clube Livelo

```
*CLUBE LIVELO: BENEFÍCIO*

📈 Oferta
· resumo da campanha

🎟️ OPÇÃO 1 — plano/modalidade
📊 pontos (mensais + bônus, total em 12 meses)
💰 Investimento: mensal / anual 12x / anual à vista — total em 12 meses de cada
🔥 Preço do milheiro: R$ X,XX (por modalidade)

🎟️ OPÇÃO 2 — ...

⚠️ Importante
· elegibilidade, prazo de crédito do bônus, cupom

🔗 Acesse:
link
```

Campanhas de "Compra de Pontos" seguem formato parecido, com o preço do milheiro
em cada cenário de desconto (descontos em cascata).

## Passo 6 — Verificação estrutural antes de enviar

`python scripts/verificar.py relatorios/AAAA-MM-DD.html` confere a contagem de
tags (article, details, footer), sobras do modelo e de dias anteriores, e varre
as frases banidas dentro de cada mensagem. Corrigir tudo até sair "OK".
(O envio se recusa a mandar um arquivo que não passa nessa verificação.)

## Passo 7 — Envio e atualização do histórico

1. `python scripts/enviar_telegram.py relatorios/AAAA-MM-DD.html` — manda pro
   Telegram SÓ as mensagens prontas, uma por oportunidade, cada uma como
   mensagem individual (pra copiar e colar no WhatsApp). O arquivo HTML não é
   enviado: ele fica no repositório como registro interno (rodapé, verificação).
   Sem oportunidade nova, vai só o aviso "Nenhuma oportunidade nova começando hoje."
2. Acrescentar uma entrada nova no topo de `historico.md` (sem apagar as
   anteriores) com loja/campanha, taxa e período de tudo que foi enviado.
3. Commit e push do HTML e do histórico no branch de trabalho.

Se depois do envio aparecer uma oportunidade que ficou de fora por engano,
reabrir o MESMO arquivo do dia (nunca criar um segundo), adicionar o card,
enviar só a mensagem nova, e documentar a correção no histórico e — se revelar falha sistemática
no método — na seção abaixo.

## Execução automática (nuvem)

- Rodar de segunda a sexta. Usar a data de hoje no fuso America/Sao_Paulo.
- Preparar o ambiente: `pip install -q -r requirements.txt`.
- Navegar com `scripts/navegar.py` (Chromium real): `texto`, `links`,
  `carrossel`, `pdf` e `js`. Seletores de página mudam; descobrir com `js`/`texto`
  quando os anteriores pararem de funcionar e anotar os que funcionaram em
  **Notas de navegação** abaixo, pra acelerar os próximos dias.
- Se um site bloquear o acesso ou não carregar, NÃO inventar resultado: seguir com
  as outras fontes, registrar no rodapé e, se faltar uma fonte primária (Livelo),
  avisar no Telegram com `scripts/enviar_telegram.py --texto "..."`.
- Segredos lidos do ambiente: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.

## Notas de navegação

(seletores e caminhos que funcionaram — atualizado pela própria rotina)

## Correções de método

(nenhuma ainda)

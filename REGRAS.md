# Rotina diária "Pega as oportunidades de hoje" — Clube Livelo + parceiros

Este é o documento de regras da rotina. A rotina agendada lê este arquivo inteiro
antes de começar. Correções de método (falhas sistemáticas descobertas depois de
um envio) são registradas na seção **Correções de método** no fim deste arquivo.

## Objetivo

Todo dia útil, montar um arquivo HTML único com as oportunidades NOVAS de
pontuação **Livelo e Esfera** (campanhas de Clube Livelo / Clube Esfera e
ofertas de parceiros/lojas nos dois programas) cujo
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

## Passo 1B — Checagem do Clube Esfera (sempre, mesmo sem novidade)

Mesma lógica do Passo 1, aplicada ao Clube Esfera (esfera.com.vc — páginas do
Clube Esfera, banners e regulamentos/termos da campanha): campanhas de
assinatura, upgrade ou bônus de Clube cujo período COMEÇA hoje. Ler o
regulamento/termos inteiro, usar preço de vitrine sem login, calcular o preço
do milheiro por modalidade (total pago em 12 meses ÷ pontos em 12 meses) e
aplicar descontos em cascata. Mensagem no template de Clube, com título
`*CLUBE ESFERA: BENEFÍCIO*`.

**Modalidades de pagamento (Clube Livelo e Clube Esfera) — conferir SEMPRE as
três:** mensal, anual parcelado (12x) e anual à vista. Cada uma tem preço
próprio e a promoção pode valer para todas ou só para algumas. Para cada
campanha de Clube:

1. Abrir a vitrine do Clube e alternar entre todas as opções de pagamento
   (abas/seletor "Mensal" / "Anual", modal "Escolha o tipo de assinatura",
   botões de cada plano) até ver o preço de cada modalidade. Não aceitar um FAQ
   ou texto genérico ("anual indisponível") como prova: só concluir que uma
   modalidade não existe depois de procurar na vitrine e no regulamento.
2. Ler no regulamento/termos para quais modalidades o bônus vale.
3. Montar uma 🎟️ OPÇÃO por plano e, dentro dela, o 💰 Investimento e o
   🔥 Preço do milheiro de CADA modalidade elegível (total pago em 12 meses ÷
   pontos em 12 meses daquela modalidade). Se o bônus só vale para algumas
   modalidades, dizer isso de forma neutra no ⚠️ Importante
   (ex.: "Bônus válido só na assinatura mensal").
4. A mensagem traz SEMPRE as três modalidades de cada plano (mensal, anual
   parcelado e anual à vista), mesmo que a vitrine pública mostre só o mensal:
   os preços anuais vêm do sistema da Esfera (ver Notas de navegação, API de
   produto) e são os mesmos que os sites de milhas publicam (ex.: campanha
   igual de julho/2026 no Pontos pra Voar, com as três modalidades). Se uma
   modalidade não existir nem no sistema, aí sim fica de fora. Se o
   regulamento restringir o bônus a uma modalidade, dizer isso de forma neutra
   no ⚠️ Importante.
5. Na dúvida sobre preço ou disponibilidade, pesquisar a campanha em sites de
   milhas (Pontos pra Voar, Passageiro de Primeira, Melhores Destinos,
   Melhores Cartões) como fonte de conferência — não como fonte primária.


## Passo 2 — Levantamento de candidatas de parceiro

Sete canais, todos obrigatórios e no mesmo nível de prioridade:

1. Filtro Ofertas/Maior pontuação da própria Livelo
2. Busca por loja na Esfera
3. Ticker principal do Compare Mania (lojas com variação verde na home)
4. Carrossel de banners em destaque no topo da página de parceiros da Livelo —
   percorrer TODOS os slides clicando repetidamente na seta de avançar (que fica
   abaixo da imagem — nunca clicar na própria imagem, que é um link pra página do
   parceiro) até o carrossel repetir o primeiro slide. O número de bolinhas
   indicadoras não é confiável como contagem. (`scripts/navegar.py carrossel` faz isso.)
5. Ofertas de parceiros da própria Esfera (página de lojas parceiras / junte
   pontos, banners e selos de bônus da Esfera) — oportunidade de juntar pontos
   Esfera vale por si só, mesmo que a Livelo não tenha nada para a loja.
6. Parceiros da Azul Fidelidade (voeazul.com.br/br/pt/programa-fidelidade/parceiros
   e voeazul.com.br/br/pt/ofertas/pontos). A listagem mostra sempre a taxa
   padrão (ex.: "R$ 1 = 1 pontos Azul"), então a promoção só aparece abrindo o
   link/regulamento de cada parceiro. Os sites da Azul recusam acesso vindo da
   nuvem (403), então: (a) procurar posts do dia nos sites de milhas (feeds
   RSS do Passageiro de Primeira e do Melhores Cartões, busca "azul fidelidade"),
   (b) cruzar as duas fontes (pontos por tier Clube Azul / demais, categorias
   excluídas, validade, prazo de crédito) e (c) abrir o link direto da loja na
   parceria (ex. Magalu: https://clube.magazineluiza.com.br/tudoazul; Natura: https://www.natura.com.br/parceiros-azul, que traz o regulamento oficial no rodapé — quando a página da loja tem o texto oficial, ele vale mais que os blogs) para
   confirmar que a campanha está no ar. A mensagem usa SEMPRE o link direto da
   loja na parceria, nunca o post do blog. Título: `*LOJA (AZUL): BENEFÍCIO*`.

7. Transferências bonificadas entre parceiros para a LATAM Pass e a Azul
   Fidelidade (qualquer parceiro de origem: bancos, cartões, hotéis, Livelo,
   Esfera…). Ver "Transferências bonificadas" abaixo.

### Transferências bonificadas (LATAM Pass e Azul)

Fontes: promoções da LATAM Pass (https://latampass.latam.com/br/pt, páginas
`/pt_br/promocao/<parceiro>-milhas-extras`) e ofertas da Azul
(https://www.voeazul.com.br/br/pt/ofertas/<parceiro>, ex. `/ofertas/sicredi`).
Os dois sites dão 403 a partir da nuvem, então: procurar nos feeds RSS dos
sites de milhas (Passageiro de Primeira, Melhores Cartões, Melhores Destinos;
buscas "latam+pass+bonus", "transferencia+bonus", "azul+fidelidade" e o feed
geral `/feed/`) os posts de bônus em transferência, ler o post inteiro e pegar
nele o link oficial da campanha (o link vai na mensagem SEM os parâmetros utm).

1. Banner: SEMPRE vai antes da mensagem (foto da promoção). Usar o banner
   oficial: a LATAM hospeda os dela em
   `latam-b75-prod.adobecqms.net/content/dam/effp/web-latampass/pt_br/banners/campaigns/...`
   (esse servidor abre da nuvem; o nome da pasta costuma trazer as datas, ex.
   `c6-14-al-1610`), e os posts trazem a URL na tag img. Para a Azul, usar a
   imagem de cabeçalho oficial da oferta (ex. arquivo `bnr-header-<parceiro>`)
   e conferir que não tem marca de blog. Salvar em `relatorios/img/AAAA-MM-DD-<programa>-<parceiro>.ext`
   e abrir o arquivo para conferir.
2. Datas: o texto do banner oficial ("Promoção válida de X a Y") vale mais que
   o post. Cruzar com um segundo site quando houver.
3. Enviar no dia em que a promoção COMEÇA e reenviar no ÚLTIMO dia com o título
   começando por `ACABA HOJE — ` (mesmo banner antes). Promoção de um dia só
   não tem reenvio. Registrar no `historico.md` com a marca
   `[TRANSF início=DD/MM fim=DD/MM]`; todo disparo diário procura no histórico
   as transferências com `fim=` igual a hoje e manda o "ACABA HOJE" (se o
   início também for hoje, não reenvia).
4. Template (negritos do WhatsApp como no exemplo):

```
*ORIGEM → DESTINO: X% DE BÔNUS (+ extras)*

📈 *Bonificação*
• *X% de bônus* sobre os pontos transferidos da ORIGEM para o DESTINO
• extras / tiers (Clube, categoria, primeira transferência)

📅 *Validade*
• De *DD/MM/AAAA* até *DD/MM/AAAA às 23h59*

⚠️ *Importante*
• cadastro obrigatório antes de transferir (se houver)
• limites por CPF, prazo de crédito e validade dos pontos bônus
• não cumulatividade, titularidade, cupons extras

🔗 Acesse:
link oficial da campanha
```

5. Template das transferências para a **Azul Fidelidade** (pedido do dono em
   15/10 — mais visual porque tem muitas faixas de bônus). Na seção "Bônus por
   tempo de Clube Azul" vai o percentual TOTAL de cada faixa (bônus do Clube +
   extra por tempo; ex.: 80% + 5% = 85%), não só o extra. "🎁 Bônus extra" só
   entra se houver (pontos na 1ª transferência, cupom etc.). O link de indicação
   do Clube Azul no final vai SEMPRE, exatamente como abaixo:

```
*ORIGEM → AZUL FIDELIDADE: ATÉ X% DE BÔNUS*

📈 Bonificação
• 50% de bônus → Clientes Azul Fidelidade
• 80% de bônus → Assinantes Clube Azul

📊 Bônus por tempo de Clube Azul
• 85% de bônus → Assinantes Clube Azul de 6 a 11 meses
• 90% de bônus → Assinantes Clube Azul de 1 a 2 anos
• 100% de bônus → Assinantes Clube Azul de 3 a 4 anos
• 110% de bônus → Assinantes Clube Azul há mais de 5 anos

🎁 Bônus extra
• Ganhe 2.000 pontos na 1ª transferência

📅 Validade
• De DD/MM/AAAA até DD/MM/AAAA

⚠️ Importante
• É necessário se cadastrar na promoção antes de transferir os pontos
• Os pontos bônus serão creditados em até 15 dias úteis após o término da campanha
• Os pontos bônus têm validade de 6 meses
• Limite de bônus por CPF: 300.000 pontos
• Limite de pontos bônus por tempo de Clube: 100.000 pontos por ano
• A transferência deve ser feita da ORIGEM para o Azul Fidelidade

🔗 Acesse:
https://www.voeazul.com.br/br/pt/ofertas/<parceiro>

Se você ainda não é assinante do Clube Azul, assine com o link abaixo e ganhe mais 1.000 milhas bônus:

https://apps.voeazul.com.br/TudoAzulClub/share-mgm.html?hash=4F4kj%2Fmf5OIYZS8t7VJ3BYWCILyy572CPnB1uR9sFIMc-a
```

   No "ACABA HOJE", o título vira `*ACABA HOJE — ORIGEM → AZUL FIDELIDADE: ATÉ X% DE BÔNUS*`
   e o resto da mensagem fica igual. Para a LATAM Pass (e outros destinos)
   segue o template do item 4.

## Passo 3 — Verificação individual de cada candidata

Pra cada loja levantada por qualquer um dos canais, entrar na página específica
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

### Foto da promoção (antes da mensagem)

Em campanhas que NÃO são de compra em parceiro — adesão/upgrade de Clube
(Livelo ou Esfera), compra de pontos, transferência bonificada e afins — a
mensagem vai precedida da imagem oficial da promoção (o banner da campanha):

1. Salvar o banner com `scripts/navegar.py imagem URL --seletor ... --saida
   relatorios/img/AAAA-MM-DD-nome.png` (de preferência a imagem original do
   banner da página da campanha ou do carrossel; senão, print só do banner).
   Conferir abrindo o arquivo que é mesmo o banner certo, sem cortes.
2. Colocar no card `<img class="banner" src="img/AAAA-MM-DD-nome.png">`.
3. O `enviar_telegram.py` manda a foto e, logo em seguida, a mensagem.

Ofertas de compra em parceiros/lojas vão só com a mensagem, sem foto.

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

## Checagem extra das 18h (Livelo — lançamentos relâmpago)

A Livelo às vezes publica campanhas novas por volta das 18h, que aparecem do
nada em livelo.com.br/regulamentos-ativos e/ou no banner inicial (carrossel do
topo de livelo.com.br e da página de parceiros). Nesse disparo:

1. Abrir livelo.com.br/regulamentos-ativos e listar os regulamentos; comparar
   com os já registrados em `historico.md` e no HTML do dia.
2. Percorrer o carrossel do banner inicial de livelo.com.br (todos os slides,
   pela seta, até repetir o primeiro) e o da página de parceiros.
3. Regulamento ou banner NOVO de campanha (Clube, compra de pontos, parceiro,
   transferência bonificada etc.) que começa hoje ou amanhã → ler o regulamento
   inteiro e aplicar as mesmas regras de verificação, cálculo e formatação.
4. Acrescentar os cards ao HTML do dia (mesmo arquivo) e enviar com
   `scripts/enviar_telegram.py relatorios/AAAA-MM-DD.html --silencioso`:
   só vai o que ainda não foi enviado, e sem novidade não vai nada.
5. Registrar no `historico.md` (na entrada do dia, marcando "18h"), commit e push.

## Checagem das 15h — Azul "Meu Resgate Favorito"

Resgates relâmpago no Shopping Azul (produtos por poucos pontos, poucas
unidades), que abrem por volta das 15h e nem todo dia. Página oficial:
https://shopping.azulfidelidade.com.br/categoria/74654/meu-resgate-favorito

Os sites da Azul (shopping.azulfidelidade.com.br, azulfidelidade.com.br,
voeazul.com.br) recusam acesso vindo da nuvem ("Access Denied" / conexão
encerrada; testado em 12/10/2026), então a checagem usa os sites de milhas que
publicam a oferta minutos depois de ela abrir (Passageiro de Primeira ~15h02–
15h15, Pontos pra Voar ~15h01–15h13):

1. O disparo começa às 14h57. PRIMEIRO de tudo (antes de reler regras,
   histórico ou qualquer outra coisa), rodar
   `/usr/bin/python3 scripts/azul_resgate.py --vigiar-ate 15:30` — ele checa as
   duas fontes a cada 30 s (~5 s por rodada) e sai no primeiro post do dia.
   "NADA" → encerrar sem enviar nada.
   Achou → mandar NA HORA um aviso curto (antes de ler os posts):
   `scripts/enviar_telegram.py --texto "*AZUL — MEU RESGATE FAVORITO NO AR!*

   <título do post sem o nome do blog>

   🔗 https://shopping.azulfidelidade.com.br/categoria/74654/meu-resgate-favorito"`
   e só depois montar a mensagem completa (passos abaixo).
2. Para a mensagem completa, tentar a página oficial com `scripts/navegar.py texto`; se abrir, ela
   é a fonte primária. Se não abrir, ler os posts encontrados (os dois, quando
   houver) e cruzar: cada produto, pontos, condições (Clube Azul / categoria,
   limite por CPF, poucas unidades). Divergência entre as fontes → usar o que
   as duas concordam e anotar no rodapé.
3. Anti-duplicata contra `historico.md` (mesmo produto e mesmos pontos já
   enviados = não reenviar).
4. Card no HTML do dia + mensagem no template abaixo, sem foto (a imagem dos
   posts tem a marca do blog). O link é sempre o da página oficial acima.
   Nunca citar os blogs na mensagem.
5. Enviar com `scripts/enviar_telegram.py relatorios/AAAA-MM-DD.html --silencioso`,
   registrar no `historico.md` (marcando "15h — Azul"), commit e push.

Template:

```
*AZUL — MEU RESGATE FAVORITO: PRODUTOS A PARTIR DE X MIL PONTOS*

🎁 Ofertas
· Produto 1 – X pontos
· Produto 2 – Y pontos

📅 Validade
· Hoje (DD/MM), enquanto durarem as unidades

⚠️ Importante
· Exclusivo para assinantes do Clube Azul e clientes com categoria
· Poucas unidades — resgate rápido
· (limite por CPF, se houver)

🔗 Acesse:
https://shopping.azulfidelidade.com.br/categoria/74654/meu-resgate-favorito
```

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

- Usar `/usr/bin/python3` (o `python` do PATH pode não enxergar o playwright instalado).
- Livelo — validade de todas as promoções de uma vez: abrir cada link da listagem com selo "Promo" em páginas paralelas (playwright async, 6 por vez) e extrair a linha "Campanha válida..." + "Termina em" + a linha após "Prazo" (prazo de crédito). Em 13/10 levou ~1 min para 41 parceiros. Atenção: algumas páginas escrevem "Campanha de X a Y" (sem "válida") ou "Válido de".
- Cards da listagem de parceiros Livelo: `a[data-testid=a_PartnerCard_card_link]` (via `js`, após rolar); filtrar por "Promo|Era|Nova" — parceiro recém-chegado vem com selo "Nova" e pode ter campanha começando no dia (Brastemp, 16/10, só achada às 18h). Página do parceiro: texto "Campanha válida de X a Y" + "Termina em ...".
- Carrossel da HOME da Livelo: mesmo container/seta, mas um pop-up (`[id^=web_modal]`) cobre a seta e o `carrossel` trava; remover antes de cada clique (`document.querySelectorAll('[id^=web_modal]').forEach(e=>e.remove())`). Em 12/10 eram 6 slides.
- O carrossel da página de parceiros também pode travar no pop-up `[id^=web_modal]` (14/10, 18h): usar a mesma remoção do pop-up da home. Em 15/10 (18h) o chat do site (`#chatbot-container`) também cobriu a seta: remover junto (`[id^=web_modal],#chatbot-container`). Banners da home sem link (ex.: Etihad Guest) não têm página de campanha na Livelo; conferir a validade pelos sites de milhas.
- Carrossel Livelo: `--container "div.swiper.css-1mcxol9" --seta "button.button-next"` (3 slides em 12/10; classes css-* podem mudar).
- Compare Mania: no texto da home cada item vem como 3 linhas: NOME / variação (+N% verde, -N% vermelho) / taxa. Filtrar variação "+" com taxa em "pt/$" (pontos; "%" é cashback). Lojas que não aparecem na Livelo nem na Esfera são de outro programa.
- Azul: voeazul.com.br / azulfidelidade.com.br dão 403 (Akamai) e magazineluiza.com.br também, mas clube.magazineluiza.com.br/tudoazul abre e mostra "Ganhe X pontos" por produto (pontuação base; o extra do Clube Azul cai depois). Links diretos das lojas aparecem nos posts do Melhores Cartões (feed `?s=azul+LOJA&feed=rss2`, procurar href com o domínio da loja).
- Esfera: digitar a loja no input da página junte-pontos/esf02163 e ler o texto depois de "Todas as categorias".
- Esfera — fonte mais rápida: artigo diário "Campanhas - DD/MM/AAAA" em esfera.zendesk.com/hc/pt-br/sections/52066838928275 (via `links`). Traz a tabela de parceiros com Data início/fim e os termos de campanhas do Clube; filtrar "Data início" = hoje e comparar com o artigo da véspera. Depois conferir cada um na página do parceiro.
- Esfera — página de parceiro: links `/p/<loja>/<id>` (ex. decolar/e000100402, hoteiscom/e000100148); com `links --rolar` em junte-pontos/esf02163 os cards mostram "Ganhe X pts a cada real". Validade em "Condições válidas para compras efetuadas de ... até ...".
- Banner do Clube Esfera (foto da promoção): `navegar.py imagem https://www.esfera.com.vc/clube --seletor 'img[src*="lpclube_header"]' --saida relatorios/img/AAAA-MM-DD-clube-esfera.png` (baixa a imagem original do header; em 12/10 veio 594x496, banner inteiro).
- Clube Esfera — preços de TODAS as modalidades: a página /clube chama apigw.esfera.com.vc/bff-product/ehcs/products/e000100211 (capturar a resposta com page.on("response")); childSKUs trazem esf_planType (monthly / yearly / yearly-installment), esf_multiplier (x0 = linha da vitrine) e salePrice. Comparar com o que a vitrine realmente oferece (config esfPlanType / seletor visível).
- Clube Esfera: a URL é esfera.com.vc/clube (/clube-esfera dá erro). Preços mensais nos cards dos planos; o banner do topo traz a campanha (nome do arquivo da imagem começa com a data AAAAMMDD). "Selecionar" exige login; o FAQ "Como posso pagar" diz se o anual está disponível.

## Correções de método

- 12/10/2026 — Clube Esfera enviado só com o preço mensal porque o FAQ dizia
  "anual indisponível". Regra nova: conferir sempre mensal, anual parcelado e
  anual à vista na vitrine e no regulamento (ver "Modalidades de pagamento"
  no Passo 1B; vale também para o Clube Livelo).
- 12/10/2026 — Preço anual escondido na vitrine não é motivo pra tirar o anual
  da mensagem: a mesma campanha de julho/2026 foi publicada pelos blogs com as
  três modalidades. Regra: sempre as três, com preços do sistema.

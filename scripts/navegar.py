"""Ajudante de navegação com Chromium real (Playwright), pra conferir tudo na página.

Uso:
  python scripts/navegar.py texto URL [--rolar] [--esperar SELETOR] [--png arquivo.png]
      Texto visível da página depois de carregar (e rolar até o fim, com --rolar).
  python scripts/navegar.py links URL [--filtro trecho]
      Lista os links (texto -> href) da página, ex.: PDFs de regulamentos.
  python scripts/navegar.py carrossel URL --container SELETOR --seta SELETOR [--max 60] [--png-dir pasta]
      Clica na seta de avançar (nunca na imagem) até o primeiro slide voltar,
      imprimindo texto/alt/link de cada slide visível.
  python scripts/navegar.py pdf URL
      Baixa um PDF (regulamento) e imprime o texto inteiro.
  python scripts/navegar.py imagem URL --seletor SELETOR --saida arquivo.png
      Salva o banner da promoção: baixa a imagem original se SELETOR for um
      <img>, senão tira print só daquele elemento.
  python scripts/navegar.py js URL "expressão JS"
      Avalia uma expressão JS na página carregada e imprime o resultado (JSON).
"""
import argparse
import io
import json
import sys

from playwright.sync_api import sync_playwright

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")

ASSINATURA_SLIDE = """(sel) => {
  const c = document.querySelector(sel);
  if (!c) return null;
  const r = c.getBoundingClientRect();
  const vis = (e) => { const b = e.getBoundingClientRect();
    const x = Math.max(0, Math.min(b.right, r.right) - Math.max(b.left, r.left));
    return b.width > 0 && x / b.width > 0.6; };
  const itens = [...c.querySelectorAll('a[href], img')].filter(vis).map(e =>
    e.tagName === 'IMG' ? 'img:' + (e.alt || '') + '|' + (e.currentSrc || e.src)
                        : 'a:' + e.href);
  const textos = [...c.querySelectorAll('*')].filter(e => e.children.length === 0 && vis(e))
    .map(e => e.innerText && e.innerText.trim()).filter(Boolean);
  return {chave: itens.join(' || '), itens, texto: [...new Set(textos)].join(' / ')};
}"""


def abrir(p, url, esperar=None, rolar=False):
    b = p.chromium.launch()
    ctx = b.new_context(user_agent=UA, locale="pt-BR", timezone_id="America/Sao_Paulo",
                        viewport={"width": 1366, "height": 900})
    pg = ctx.new_page()
    pg.goto(url, wait_until="domcontentloaded", timeout=90000)
    try:
        pg.wait_for_load_state("networkidle", timeout=30000)
    except Exception:
        pass
    if esperar:
        pg.wait_for_selector(esperar, timeout=30000)
    if rolar:
        altura = 0
        for _ in range(60):
            pg.mouse.wheel(0, 1500)
            pg.wait_for_timeout(500)
            nova = pg.evaluate("document.body.scrollHeight")
            if nova == altura:
                break
            altura = nova
    return b, pg


def main():
    a = argparse.ArgumentParser()
    a.add_argument("modo", choices=["texto", "links", "carrossel", "pdf", "js", "imagem"])
    a.add_argument("url")
    a.add_argument("expr", nargs="?")
    a.add_argument("--rolar", action="store_true")
    a.add_argument("--esperar")
    a.add_argument("--png")
    a.add_argument("--filtro", default="")
    a.add_argument("--container")
    a.add_argument("--seta")
    a.add_argument("--max", type=int, default=60)
    a.add_argument("--png-dir")
    a.add_argument("--seletor")
    a.add_argument("--saida")
    args = a.parse_args()

    with sync_playwright() as p:
        if args.modo == "pdf":
            from pypdf import PdfReader
            ctx = p.request.new_context(extra_http_headers={"User-Agent": UA})
            r = ctx.get(args.url, timeout=90000)
            if not r.ok:
                sys.exit(f"HTTP {r.status} ao baixar {args.url}")
            leitor = PdfReader(io.BytesIO(r.body()))
            for i, pag in enumerate(leitor.pages, 1):
                print(f"\n===== página {i}/{len(leitor.pages)} =====")
                print(pag.extract_text() or "")
            return

        b, pg = abrir(p, args.url, args.esperar, args.rolar)
        if args.modo == "texto":
            print(pg.inner_text("body"))
            if args.png:
                pg.screenshot(path=args.png, full_page=True)
        elif args.modo == "links":
            for t, h in pg.evaluate("[...document.querySelectorAll('a[href]')].map(a => [a.innerText.trim(), a.href])"):
                if args.filtro.lower() in (t + h).lower():
                    print(f"{t[:80]!r} -> {h}")
        elif args.modo == "imagem":
            if not (args.seletor and args.saida):
                sys.exit("imagem precisa de --seletor e --saida")
            el = pg.locator(args.seletor).first
            el.scroll_into_view_if_needed()
            src = el.evaluate("e => e.tagName === 'IMG' ? (e.currentSrc || e.src) : null")
            try:
                r = pg.request.get(src) if src else None
            except Exception:
                r = None
            if r is not None and r.ok and r.headers.get("content-type", "").startswith("image/"):
                with open(args.saida, "wb") as f:
                    f.write(r.body())
            else:
                el.screenshot(path=args.saida)
            print(f"salvo: {args.saida}")
        elif args.modo == "js":
            print(json.dumps(pg.evaluate(args.expr), ensure_ascii=False, indent=1))
        elif args.modo == "carrossel":
            if not (args.container and args.seta):
                sys.exit("carrossel precisa de --container e --seta")
            vistos = []
            for i in range(args.max + 1):
                s = pg.evaluate(ASSINATURA_SLIDE, args.container)
                if s is None:
                    sys.exit(f"container {args.container!r} não encontrado")
                if vistos and s["chave"] == vistos[0]["chave"]:
                    print(f"\n>>> Voltou ao primeiro slide: {len(vistos)} slide(s) distintos vistos.")
                    break
                vistos.append(s)
                print(f"\n--- slide {len(vistos)} ---\n{s['texto']}\n" + "\n".join(s["itens"]))
                if args.png_dir:
                    pg.locator(args.container).screenshot(path=f"{args.png_dir}/slide{len(vistos):02d}.png")
                pg.locator(args.seta).first.click()
                pg.wait_for_timeout(1200)
            else:
                print(f"\n>>> ATENÇÃO: atingiu --max={args.max} sem voltar ao primeiro slide.")
        b.close()


if __name__ == "__main__":
    main()

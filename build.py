#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kryptooo static site generator.

Usage:   python3 build.py
Output:  ./public   (upload this folder to any static host)
Preview: python3 -m http.server 8080 -d public

EDIT THE CONFIG BELOW before publishing. Every page, sitemap, ads.txt and
structured-data block is regenerated from these values.
"""
import html, random, re, shutil
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).parent / "src"))
from content import ARTICLES, GLOSSARY, PAGES

# ============================ CONFIG ======================================
CONFIG = {
    "DOMAIN":      "www.kryptooo.example",      # your real domain, no https://
    "COMPANY":     "kryptooo",                  # legal / trading name shown in policies
    "EMAIL":       "contact@kryptooo.example",
    "PRIVACY_EMAIL": "privacy@kryptooo.example",
    "AD_EMAIL":    "advertising@kryptooo.example",
    "CORR_EMAIL":  "corrections@kryptooo.example",
    "ADDRESS":     "",                          # postal address; shown on About and Contact when set
    "ADSENSE_PUB": "",                          # e.g. "pub-1234567890123456"; empty = no ads, no ad scripts
    "ADSENSE_SLOT": "0000000000",               # your ad unit id
    "UPDATED":     "October 11, 2026",
    "UPDATED_ISO": "2026-10-11",
}
# ==========================================================================

C = CONFIG
SRC = Path(__file__).parent / "src"
OUT = Path(__file__).parent / "public"
BASE = f"https://{C['DOMAIN']}"

def esc(s): return html.escape(s, quote=True)

def tokens(s):
    addr = f'<p><strong>Mailing address:</strong> {esc(C["ADDRESS"])}</p>' if C["ADDRESS"] else ""
    m = {"[[COMPANY]]": C["COMPANY"], "[[DOMAIN]]": C["DOMAIN"], "[[EMAIL]]": C["EMAIL"],
         "[[PRIVACY_EMAIL]]": C["PRIVACY_EMAIL"], "[[AD_EMAIL]]": C["AD_EMAIL"], "[[CORR_EMAIL]]": C["CORR_EMAIL"],
         "[[UPDATED]]": C["UPDATED"], "[[ADDRESS_LINE]]": addr}
    for k, v in m.items(): s = s.replace(k, v)
    return s

def rootify(s, root):
    """Content uses root-absolute hrefs; convert to relative so the site also works from a folder."""
    return s.replace('href="/', f'href="{root}')

def slugify(t): return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", t).lower()).strip("-")

def add_ids(body):
    toc = []
    def sub(m):
        title = m.group(1); sid = slugify(title); toc.append((sid, re.sub(r"<[^>]+>", "", html.unescape(title))))
        return f'<h2 id="{sid}">{title}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", sub, body), toc

def ad():
    if not C["ADSENSE_PUB"]: return ""
    return ('<aside class="ad" aria-label="Advertisement"><span class="ad-l">Advertisement</span>'
            f'<ins class="adsbygoogle" style="display:block" data-ad-client="ca-{C["ADSENSE_PUB"]}" '
            f'data-ad-slot="{C["ADSENSE_SLOT"]}" data-ad-format="auto" data-full-width-responsive="true"></ins></aside>')

# ----------------------------- shared chrome ------------------------------
NAV = [("Markets", "index.html", "home"), ("Learn", "learn/index.html", "learn"),
       ("Glossary", "glossary.html", "glossary"), ("About", "about.html", "about"), ("Contact", "contact.html", "contact")]

def sprite():
    s = (SRC / "sprite.html").read_text(encoding="utf-8")
    extra = ('<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>'
             '<symbol id="i-chev" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></symbol>'
             '<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>'
             '<symbol id="i-book" viewBox="0 0 24 24"><path d="M5 5.5A2.5 2.5 0 0 1 7.5 3H19v15H7.5A2.5 2.5 0 0 0 5 20.5zM5 20.5A2.5 2.5 0 0 0 7.5 23H19"/></symbol>')
    return s.replace("</defs>", extra + "</defs>")

def header(active, market, root):
    links = "".join(f'<a href="{root}{h}"' + (' aria-current="page"' if k == active else "") + f">{t}</a>" for t, h, k in NAV)
    mlinks = "".join(f'<li><a href="{root}{h}"' + (' aria-current="page"' if k == active else "") + f">{t}</a></li>" for t, h, k in NAV)
    search = '''<div class="search" id="navSearch">
      <svg class="ic" aria-hidden="true"><use href="#i-search"/></svg>
      <label class="sr-only" for="q">Search symbols and names</label>
      <input id="q" type="search" autocomplete="off" spellcheck="false" placeholder="Search symbols or names" role="combobox" aria-expanded="false" aria-controls="qList" aria-autocomplete="list">
      <span class="kbd" aria-hidden="true">/</span>
      <ul class="results" id="qList" role="listbox" aria-label="Search results" hidden></ul></div>''' if market else ""
    mk = '''<div class="mode" role="group" aria-label="Asset class"><span class="thumb" aria-hidden="true"></span>
        <button type="button" data-mode="stock" aria-pressed="true">Stocks</button>
        <button type="button" data-mode="crypto" aria-pressed="false">Crypto</button></div>
      <button type="button" class="ibtn" id="wlJump" aria-label="Go to watchlist"><svg class="ic" aria-hidden="true"><use href="#i-list"/></svg><span class="badge" id="wlCount">0</span></button>''' if market else ""
    return f'''<header class="nav">
  <div class="wrap nav-in{' has-search' if market else ''}">
    <a class="logo" href="{root}index.html" aria-label="kryptooo home"><svg class="ic" aria-hidden="true"><use href="#logo"/></svg><span>kryptooo</span></a>
    <nav class="pnav" aria-label="Primary">{links}</nav>
    {search}
    <div class="actions">{mk}
      <button type="button" class="ibtn" id="themeBtn" aria-label="Switch to light theme"><svg class="ic i-sun" aria-hidden="true"><use href="#i-sun"/></svg><svg class="ic i-moon" aria-hidden="true"><use href="#i-moon"/></svg></button>
      <button type="button" class="ibtn menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false" aria-controls="mnav"><svg class="ic" aria-hidden="true"><use href="#i-menu"/></svg></button>
    </div>
  </div>
  <nav class="mnav" id="mnav" aria-label="Mobile" hidden><ul>{mlinks}</ul></nav>
</header>'''

def footer(root):
    L = lambda h, t: f'<li><a href="{root}{h}">{t}</a></li>'
    return f'''<footer>
  <div class="wrap">
    <div class="f-top">
      <div class="f-brand">
        <a class="logo" href="{root}index.html"><svg class="ic" aria-hidden="true"><use href="#logo"/></svg><span>kryptooo</span></a>
        <p>A markets information site that reads equities, digital assets and indices side by side, with plain-language guides.</p>
      </div>
      <nav class="f-cols" aria-label="Footer">
        <div><h4>Markets</h4><ul>{L("index.html#movers","Stock movers")}{L("index.html#crypto","Crypto market")}{L("index.html#map","Market map")}{L("index.html#map","Watchlist")}</ul></div>
        <div><h4>Learn</h4><ul>{L("learn/index.html","All guides")}{L("glossary.html","Glossary")}{L("learn/how-to-read-a-stock-quote.html","Reading a quote")}{L("learn/stocks-vs-crypto.html","Stocks vs crypto")}</ul></div>
        <div><h4>Company</h4><ul>{L("about.html","About")}{L("contact.html","Contact")}{L("editorial-policy.html","Editorial policy")}{L("advertising-policy.html","Advertising policy")}</ul></div>
        <div><h4>Legal</h4><ul>{L("privacy-policy.html","Privacy policy")}{L("terms-of-service.html","Terms of service")}{L("cookie-policy.html","Cookie policy")}{L("disclaimer.html","Disclaimer")}<li><button type="button" id="cookiePrefs">Cookie preferences</button></li></ul></div>
      </nav>
    </div>
    <p class="disc"><svg class="ic" aria-hidden="true"><use href="#i-shield"/></svg>
      <span>Prices, volumes, indices and charts on this site are simulated for demonstration. kryptooo is not a broker or adviser, and nothing here is investment advice or an offer to trade. Read the <a href="{root}disclaimer.html" style="text-decoration:underline">full disclaimer</a>.</span></p>
    <div class="f-bot">
      <span>&copy; <span id="yr">2026</span> {esc(C["COMPANY"])}. All rights reserved.</span>
      <nav aria-label="Legal"><a href="{root}privacy-policy.html">Privacy</a><a href="{root}terms-of-service.html">Terms</a><a href="{root}cookie-policy.html">Cookies</a><a href="{root}sitemap.html">Sitemap</a></nav>
    </div>
  </div>
</footer>'''

def jsonld_org(root):
    return ('{"@context":"https://schema.org","@graph":['
            f'{{"@type":"Organization","@id":"{BASE}/#org","name":"{esc(C["COMPANY"])}","url":"{BASE}/","logo":"{BASE}/assets/logo.svg","email":"{C["EMAIL"]}"}},'
            f'{{"@type":"WebSite","@id":"{BASE}/#site","url":"{BASE}/","name":"kryptooo","publisher":{{"@id":"{BASE}/#org"}}}}]}}')

def page(path, title, desc, body, active="", market=False, extra_ld="", body_cls="", og_type="website", home_tape=False):
    root = "../" * path.count("/")
    pub = f'<meta name="adsense-client" content="ca-{C["ADSENSE_PUB"]}">\n' if C["ADSENSE_PUB"] else ""
    full_title = title if title.startswith("kryptooo") else f"{title} | kryptooo"
    market_js = f'<script src="{root}assets/market.js" defer></script>\n' if market else ""
    canon = f"{BASE}/{path}" if path != "index.html" else f"{BASE}/"
    doc = f'''<!doctype html>
<html lang="en" data-theme="dark" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0a1020">
<link rel="canonical" href="{canon}">
<link rel="icon" href="{root}assets/logo.svg" type="image/svg+xml">
<meta property="og:site_name" content="kryptooo">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
{pub}<script>try{{var t=localStorage.getItem('kryptooo_theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="stylesheet" href="{root}assets/styles.css">
<script type="application/ld+json">{jsonld_org(root)}</script>
{extra_ld}</head>
<body class="{body_cls}" data-mode="stock">
{sprite()}
<a class="skip" href="#main">Skip to content</a>
{header(active, market, root)}
{body}
{footer(root)}
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="{root}assets/site.js" defer></script>
{market_js}</body>
</html>'''
    doc = rootify(doc, root)
    p = OUT / path; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(doc, encoding="utf-8")

# ------------------------------ page types --------------------------------
def crumbs(items):
    out = []
    for i, (t, h) in enumerate(items):
        out.append(f'<a href="/{h}">{t}</a>' if h else f'<span aria-current="page">{t}</span>')
    sep = '<svg class="ic" aria-hidden="true"><use href="#i-chev"/></svg>'
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb">{sep.join(out)}</nav>'

def prose_page(slug, d):
    body, toc = add_ids(tokens(d["body"]))
    toc_html = ""
    if d.get("toc") and toc:
        toc_html = '<nav class="toc" aria-label="On this page"><h2>On this page</h2><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc) + "</ol></nav>"
    upd = f'<span class="updated">Last updated {C["UPDATED"]}</span>' if d.get("updated") else ""
    main = f'''<main id="main">
{crumbs([("Home","index.html"),(d["title"],None)])}
<header class="page-hero wrap"><h1>{esc(d["title"])}</h1><p class="lede">{esc(d["lede"])}</p>{f'<div class="meta">{upd}</div>' if upd else ""}</header>
<div class="wrap layout{'' if toc_html else ' one'}">{toc_html}<div class="prose">{body}</div></div>
</main>'''
    page(f"{slug}.html", d["title"], d["desc"], main, active=slug if slug in ("about", "contact") else "")

def article_page(a):
    body, toc = add_ids(a["body"])
    toc_html = '<nav class="toc" aria-label="On this page"><h2>On this page</h2><ol>' + "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc) + "</ol></nav>"
    take = '<div class="note"><strong>Key takeaways</strong><ul>' + "".join(f"<li>{t}</li>" for t in a["takeaways"]) + "</ul></div>"
    # one ad after the intro block, one before the related list (labeled, not near navigation)
    related = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
    rel = '<div class="article-foot"><h2 style="font-size:18px;font-weight:640">Keep reading</h2><div class="related">' + "".join(
        f'<a href="/learn/{r["slug"]}.html">{esc(r["title"])}<span>{r["read"]} min</span></a>' for r in related) + "</div></div>"
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
          f'"headline":"{esc(a["title"])}","description":"{esc(a["desc"])}","datePublished":"{C["UPDATED_ISO"]}","dateModified":"{C["UPDATED_ISO"]}",'
          f'"author":{{"@type":"Organization","name":"{esc(C["COMPANY"])} Editorial"}},"publisher":{{"@id":"{BASE}/#org"}},'
          f'"mainEntityOfPage":"{BASE}/learn/{a["slug"]}.html"}}</script>\n')
    main = f'''<main id="main">
{crumbs([("Home","index.html"),("Learn","learn/index.html"),(a["title"],None)])}
<header class="page-hero wrap"><h1>{esc(a["title"])}</h1><p class="lede">{esc(a["lede"])}</p>
<div class="meta"><span class="tag">{a["tag"]}</span><span>{a["read"]} min read</span><span class="updated">Last updated {C["UPDATED"]}</span><span>By {esc(C["COMPANY"])} Editorial. <a href="/editorial-policy.html" style="text-decoration:underline">How we write</a></span></div></header>
<div class="wrap layout">{toc_html}<article class="prose">{take}{ad()}{body}{ad()}{rel}</article></div>
</main>'''
    page(f"learn/{a['slug']}.html", a["title"], a["desc"], main, active="learn", extra_ld=ld, og_type="article")

def learn_hub():
    cards = "".join(
        f'<a class="card" href="/learn/{a["slug"]}.html"><div class="meta"><span class="tag">{a["tag"]}</span><span>{a["read"]} min read</span></div>'
        f'<h3>{esc(a["title"])}</h3><p>{esc(a["desc"])}</p><span class="more">Read guide <svg class="ic" aria-hidden="true"><use href="#i-arrow"/></svg></span></a>'
        for a in ARTICLES)
    main = f'''<main id="main">
{crumbs([("Home","index.html"),("Learn",None)])}
<header class="page-hero wrap"><h1>Learn how markets work</h1><p class="lede">Plain-language guides to reading quotes, understanding indices and comparing stocks with crypto. New to a term? Check the <a href="/glossary.html" style="color:var(--accent);text-decoration:underline">glossary</a>.</p></header>
<div class="wrap"><div class="cards">{cards}</div>{ad()}</div>
</main>'''
    page("learn/index.html", "Learn", "Guides to reading stock quotes, market capitalization, indices, crypto sentiment and diversification.", main, active="learn")

def glossary_page():
    terms = sorted(GLOSSARY, key=lambda t: re.sub(r"[^a-z0-9]", "", t[0].lower()) or "0")
    letters = sorted({(t[0][0].upper() if t[0][0].isalpha() else "#") for t in terms})
    az = '<div class="az" aria-label="Jump to letter">' + "".join(f'<a href="#L{l}">{l}</a>' for l in letters) + "</div>"
    seen, items = set(), []
    for t, d in terms:
        l = t[0].upper() if t[0].isalpha() else "#"
        anchor = f' id="L{l}"' if l not in seen else ""
        seen.add(l)
        items.append(f'<div{anchor} style="scroll-margin-top:96px"><dt id="{slugify(t)}">{t}</dt><dd>{d}</dd></div>')
    main = f'''<main id="main">
{crumbs([("Home","index.html"),("Glossary",None)])}
<header class="page-hero wrap"><h1>Market glossary</h1><p class="lede">{len(terms)} terms used across kryptooo, defined in a sentence or two.</p></header>
<div class="wrap layout one"><div>{az}<dl class="gloss">{"".join(items)}</dl></div></div>
</main>'''
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"DefinedTermSet","name":"kryptooo market glossary","hasDefinedTerm":[' +
          ",".join(f'{{"@type":"DefinedTerm","name":"{esc(t)}","description":"{esc(re.sub("<[^>]+>","",html.unescape(d)))}"}}' for t, d in terms) + "]}</script>\n")
    page("glossary.html", "Market glossary", "Definitions of common stock market and cryptocurrency terms, from bid and ask to market capitalization.", main, active="glossary", extra_ld=ld)

def sitemap_page():
    def ul(items): return "<ul>" + "".join(f'<li><a href="/{h}">{t}</a></li>' for t, h in items) + "</ul>"
    body = ("<h2>Main</h2>" + ul([("Markets dashboard", "index.html"), ("Learn", "learn/index.html"), ("Glossary", "glossary.html")]) +
            "<h2>Guides</h2>" + ul([(a["title"], f'learn/{a["slug"]}.html') for a in ARTICLES]) +
            "<h2>Company</h2>" + ul([("About", "about.html"), ("Contact", "contact.html"), ("Editorial policy", "editorial-policy.html"), ("Advertising policy", "advertising-policy.html")]) +
            "<h2>Legal</h2>" + ul([("Privacy policy", "privacy-policy.html"), ("Terms of service", "terms-of-service.html"), ("Cookie policy", "cookie-policy.html"), ("Disclaimer", "disclaimer.html")]))
    main = f'''<main id="main">
{crumbs([("Home","index.html"),("Sitemap",None)])}
<header class="page-hero wrap"><h1>Sitemap</h1><p class="lede">Every page on kryptooo in one place.</p></header>
<div class="wrap layout one"><div class="prose">{body}</div></div></main>'''
    page("sitemap.html", "Sitemap", "A complete list of pages on kryptooo.", main)

def not_found():
    main = '''<main id="main"><div class="wrap nf"><div class="big" aria-hidden="true">404</div><h1 style="font-size:28px;letter-spacing:-.03em">This page is not on the tape</h1>
<p>The address may be mistyped, or the page may have moved. Try the dashboard or the guides.</p>
<a class="btn" href="/index.html">Back to markets</a> <a class="btn ghost" href="/learn/index.html">Browse guides</a></div></main>'''
    page("404.html", "Page not found", "The page you were looking for could not be found.", main)

def home():
    cs = random.Random(7); N = 46; v = 100.0; c = []
    for _ in range(N):
        o = v; v = o + (cs.random() - .46) * 7
        c.append((o, v, max(o, v) + cs.random() * 4, min(o, v) - cs.random() * 4))
    W, H = 640, 260; mn = min(x[3] for x in c); mx = max(x[2] for x in c)
    Y = lambda q: 30 + (1 - (q - mn) / (mx - mn)) * (H - 60); bw = W / N; svg = ""
    for i, (o, cl, hi, lo) in enumerate(c):
        col = "var(--up)" if cl >= o else "var(--dn)"; cx = i * bw + bw / 2
        svg += (f'<line x1="{cx:.1f}" x2="{cx:.1f}" y1="{Y(hi):.1f}" y2="{Y(lo):.1f}" stroke="{col}" stroke-width="1.5" opacity=".55"/>'
                f'<rect x="{cx - bw*.3:.1f}" width="{bw*.6:.1f}" y="{Y(max(o, cl)):.1f}" height="{max(2, abs(Y(o) - Y(cl))):.1f}" rx="1.5" fill="{col}" opacity=".7"/>')
    ma = [sum(x[1] for x in c[max(0, i - 7):i + 1]) / len(c[max(0, i - 7):i + 1]) for i in range(N)]
    svg += '<path d="' + "".join(("L" if i else "M") + f"{i*bw+bw/2:.1f} {Y(q):.1f}" for i, q in enumerate(ma)) + '" fill="none" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    f = ARTICLES[0]; rest = ARTICLES[1:]
    feat = (f'<a class="card feat-card" href="/learn/{f["slug"]}.html"><div class="feat-viz" aria-hidden="true"><svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">{svg}</svg></div>'
            f'<div class="fb"><div class="meta"><span class="tag">{f["tag"]}</span><span>{f["read"]} min read</span></div><h3>{esc(f["title"])}</h3><p>{esc(f["lede"])}</p>'
            '<span class="more">Read guide <svg class="ic" aria-hidden="true"><use href="#i-arrow"/></svg></span></div></a>')
    lst = "".join(f'<li><a href="/learn/{a["slug"]}.html"><div class="meta"><span class="tag">{a["tag"]}</span><span>{a["read"]} min read</span></div><h3>{esc(a["title"])}</h3></a></li>' for a in rest)
    learn = f'''  <section class="wrap sec" id="learn" aria-labelledby="lnT">
    <div class="sec-h"><h2 id="lnT">Learn the markets</h2><p>Plain-language guides, written to explain how things work. <a class="sec-more" href="/learn/index.html">All guides</a></p></div>
    {ad()}
    <div class="home-learn">{feat}<div class="panel"><ul class="l-list">{lst}</ul></div></div>
  </section>'''
    body = (SRC / "home_main.html").read_text(encoding="utf-8").replace("[[LEARN_SECTION]]", learn)
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"kryptooo markets dashboard",'
          '"description":"Live-style dashboard for US large-cap stocks, major cryptocurrencies and benchmark indices (simulated data)."}</script>\n')
    page("index.html", "kryptooo | Stocks and crypto on one tape",
         "Follow US large-cap stocks, major cryptocurrencies and benchmark indices on one tape, with charts, a market map, a watchlist and plain-language guides. Data is simulated for demonstration.",
         body, active="home", market=True, body_cls="is-loading", extra_ld=ld)

# ---------------------------- assets + SEO files --------------------------
def assets():
    a = OUT / "assets"; a.mkdir(parents=True, exist_ok=True)
    css = (SRC / "base.css").read_text(encoding="utf-8").replace("/*NAV_PLACEHOLDER*/", "") + "\n" + (SRC / "extra.css").read_text(encoding="utf-8")
    (a / "styles.css").write_text(css, encoding="utf-8")
    for f in ("site.js", "market.js"): shutil.copy(SRC / f, a / f)
    (a / "logo.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#0a1020"/>'
        '<path d="M7.5 4.5v15M7.5 13l7.2-6.5M10 11l6.5 8.5" fill="none" stroke="#e8edf6" stroke-width="1.7" stroke-linecap="round"/><circle cx="16" cy="5.8" r="2.1" fill="#f2b544"/></svg>', encoding="utf-8")

def seo_files():
    urls = ["index.html", "learn/index.html", "glossary.html", "about.html", "contact.html", "editorial-policy.html", "advertising-policy.html",
            "privacy-policy.html", "terms-of-service.html", "cookie-policy.html", "disclaimer.html", "sitemap.html"] + [f"learn/{a['slug']}.html" for a in ARTICLES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f'  <url><loc>{BASE}/{"" if u == "index.html" else u}</loc><lastmod>{C["UPDATED_ISO"]}</lastmod></url>\n' for u in urls) + "</urlset>\n"
    (OUT / "sitemap.xml").write_text(xml, encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    ads = (f"google.com, {C['ADSENSE_PUB']}, DIRECT, f08c47fec0942fa0\n" if C["ADSENSE_PUB"]
           else "# Add your line after AdSense approval, using your own publisher ID:\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
    (OUT / "ads.txt").write_text(ads, encoding="utf-8")

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    assets(); home(); learn_hub(); glossary_page(); sitemap_page(); not_found()
    for slug, d in PAGES.items(): prose_page(slug, d)
    for a in ARTICLES: article_page(a)
    seo_files()
    print("Built", sum(1 for _ in OUT.rglob("*.html")), "pages into", OUT)

if __name__ == "__main__":
    main()

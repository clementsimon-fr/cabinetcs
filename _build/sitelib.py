import os, urllib.parse, shutil, hashlib
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MAIL = "clement.simon@cabinetcs.fr"
TEL = "06 77 30 01 27"
TELH = "+33677300127"

P = {
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.8 3.2-6 6.5-6s5.9 2.2 6.5 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14c2 .7 3.2 2.7 3.5 6"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4.5 4-7 8-7s7.2 2.5 8 7"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "heart": '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "zap": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "usercheck": '<circle cx="9" cy="8" r="4"/><path d="M2 21c.8-4.5 3.6-7 7-7s6.2 2.5 7 7"/><path d="M16 11l2 2 4-4"/>',
 "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "book": '<path d="M4 19.5V5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2z"/><path d="M8 7h8"/>',
 "tree": '<path d="M12 21v-7"/><path d="M12 14c-4 0-7-2.5-7-6a5 5 0 0 1 7-4.6A5 5 0 0 1 19 8c0 3.5-3 6-7 6z"/>',
 "pin": '<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
 "phone": '<path d="M6 3h3l1.5 4-2 1.5a11 11 0 0 0 6 6l1.5-2 4 1.5v3a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
 "lr": '<path d="M4 9h16M16 5l4 4-4 4M20 15H4M8 11l-4 4 4 4"/>',
 "chev": '<path d="M6 9l6 6 6-6"/>',
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
 "building": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
 "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
 "balance": '<path d="M12 4v16M7 20h10M4 8h16M4 8l-2.5 6h5zM20 8l-2.5 6h5z"/>',
 "flag": '<path d="M5 21V4M5 4h12l-2.5 4L17 12H5"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="M6 6l12 12M18 6L6 18"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
 "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 13l2 2 4-4"/>',
 "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
 "msg": '<path d="M4 5h16v11H9l-5 4z"/>',
}
def ic(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'

# Offres : (adresse, titre, illustration, description courte)
ORG_IND = ("/organisations/coaching-individuel/", "Coaching individuel", "/assets/img/collaborateur.jpg", "Un manager, un cadre, un collaborateur")
ORG_COL = ("/organisations/coaching-collectif/", "Coaching collectif", "/assets/img/equipe.jpg", "Une équipe, un comité de direction, un groupe projet")
DIR = ("/dirigeants-entrepreneurs/", "Dirigeants & entrepreneurs", "/assets/img/olivier.jpg", "Sous l’Olivier, un espace de ressourcement")
OFFERS = [ORG_IND, ORG_COL, DIR]

def mailto(subject):
    return f"mailto:{MAIL}?subject={urllib.parse.quote(subject)}"

def header(active):
    def cur(k): return ' aria-current="page"' if active == k else ''
    org_cls = ' class="in-section"' if active in ("org-ind", "org-col") else ''
    sub = "".join(f'<li><a href="{u}"{cur(k)}><img src="{img}" alt="" width="44" height="44"><span><b>{t}</b><span>{d}</span></span></a></li>' for k,(u,t,img,d) in [("org-ind",ORG_IND),("org-col",ORG_COL)])
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap hdr">
    <a class="brand" href="/"><img src="/assets/logo.png" alt="" width="42" height="42"><span><b>Cabinet CS</b><small>Clément Simon · Coach professionnel</small></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{ic("menu","ic i-open")}{ic("close","ic i-close")}<span>Menu</span></button>
    <nav id="nav" class="nav" aria-label="Menu principal">
      <ul>
        <li><a href="/"{cur("home")}>Accueil</a></li>
        <li class="has-sub"><button type="button" class="nav-parent{" in-section" if org_cls else ""}" aria-haspopup="true">Organisations {ic("chev","ic chev")}</button>
          <ul class="sub">{sub}</ul>
        </li>
        <li><a href="{DIR[0]}"{cur("dir")}>Dirigeants &amp; entrepreneurs</a></li>
        <li><a href="/a-propos/"{cur("about")}>À propos</a></li>
        <li><a href="/contact/"{cur("contact")}>Contact</a></li>
        <li class="nav-cta"><a class="btn sm" href="/contact/">Prendre rendez-vous</a></li>
      </ul>
    </nav>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="ft">
      <div>
        <a class="brand" href="/"><img src="/assets/logo.png" alt="" width="42" height="42"><span><b>Cabinet CS</b><small>Clément Simon · Coach professionnel certifié</small></span></a>
        <p>Coaching des managers et des équipes pour les organisations. Espace de ressourcement pour les dirigeants et entrepreneurs. Au cabinet à Bourgoin-Jallieu, en visio ou dans vos locaux.</p>
      </div>
      <nav aria-label="Accompagnements"><h2>Accompagnements</h2><ul><li><a href="{ORG_IND[0]}">Coaching individuel</a></li><li><a href="{ORG_COL[0]}">Coaching collectif</a></li><li><a href="{DIR[0]}">Sous l’Olivier, dirigeants &amp; entrepreneurs</a></li></ul></nav>
      <div><h2>Contact</h2><ul><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="tel:{TELH}">{TEL}</a></li><li>Bourgoin-Jallieu (38)</li><li><a href="/contact/">Prendre rendez-vous</a></li></ul></div>
    </div>
    <div class="ft-bottom"><span>© Cabinet CS · Clément Simon</span><span><a href="/a-propos/">À propos</a> · <a href="/mentions-legales/">Mentions légales</a></span></div>
  </div>
</footer>'''

def ver(f):
    return hashlib.md5(open(ROOT + f, "rb").read()).hexdigest()[:8]

def page(path, title, desc, active, body, noindex=False):
    canon = "https://cabinetcs.fr" + path
    robots = '<meta name="robots" content="noindex">\n' if noindex else ''
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Cabinet CS">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="https://cabinetcs.fr/assets/portrait.jpg">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="/assets/logo.png">
<link rel="apple-touch-icon" href="/assets/logo.png">
<link rel="preload" href="/assets/fonts/Inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/inter.css">
<link rel="stylesheet" href="/assets/site.css?v={ver('/assets/site.css')}">
<script src="/assets/site.js?v={ver('/assets/site.js')}" defer></script>
</head>
<body>
{header(active)}
<main id="contenu">
{body}
</main>
{footer()}
</body>
</html>
'''
    out = ROOT + (path if path.endswith(".html") else path + "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)

# ---------- composants ----------
def sec(id_, inner, cls="", kicker="", h2="", sub="", center=True, narrow=False):
    head = ""
    if h2:
        k = f'<p class="kicker">{kicker}</p>' if kicker else ''
        s = f'<p class="sub-t">{sub}</p>' if sub else ''
        head = f'<div class="sec-head{" center" if center else ""}">{k}<h2 id="h-{id_}">{h2}</h2>{s}</div>'
    lab = f' aria-labelledby="h-{id_}"' if h2 else ''
    w = "wrap narrow" if narrow else "wrap"
    return f'<section id="{id_}" class="section {cls}"{lab}><div class="{w}">{head}{inner}</div></section>\n'

def cta_band(title="Envie d’en parler ?", text="Un rendez-vous découverte de 30 minutes, offert, en visio ou en présentiel, pour clarifier votre situation. Sans engagement.", subject="Prise de rendez-vous"):
    return f'''<section class="cta-band" aria-labelledby="h-cta"><div class="wrap inner">{ic("heart","ic big")}<h2 id="h-cta">{title}</h2><p class="lead">{text}</p>
<div class="btns"><a class="btn" href="/contact/">Prendre rendez-vous {ic("arrow")}</a><a class="btn ghost" href="tel:{TELH}">{ic("phone")}{TEL}</a></div></div></section>\n'''

def cards_row(items):  # (icon,title,desc)
    return '<div class="grid2">' + "".join(f'<div class="card row"><span class="chip-ic">{ic(i)}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in items) + '</div>'

def pillars(items):
    return '<ol class="pillars">' + "".join(f'<li><h3>{ic(i)}{t}</h3><p>{d}</p></li>' for i,t,d in items) + '</ol>'

def mores(items, cols=3):
    return f'<div class="grid{cols} mores">' + "".join(f'<details class="more"><summary><b>{t}</b><span>{s}</span></summary><p class="det">{d}</p></details>' for t,s,d in items) + '</div>'

def situations(items, cols=1):
    # items : (titre, contexte, demande, travail, résultat)
    out = f'<div class="sits{" grid" + str(cols) if cols > 1 else ""}">'
    for t,c,d,w,r in items:
        out += f'<article class="sit"><h3>{t}</h3><dl><div><dt>Contexte</dt><dd>{c}</dd></div><div><dt>Demande</dt><dd>{d}</dd></div><div><dt>Travail</dt><dd>{w}</dd></div><div class="res"><dt>Résultat</dt><dd>{r}</dd></div></dl></article>'
    return out + '</div>'

DISCLAIMER = '<p class="disclaimer">Des exemples illustratifs, inspirés de demandes fréquentes en accompagnement. Ce ne sont pas des témoignages de clients.</p>'

def discovery(note):
    v = "".join(f'<div><span class="L">{a}</span><b>{b}</b><p>{c}</p></div>' for a,b,c in [("V","Vision","Où souhaitez-vous aller ? Quel est votre horizon ?"),("S","Sens","Pourquoi est-ce important pour vous aujourd’hui ?"),("B","Besoin","De quoi avez-vous besoin concrètement ?")])
    return f'''<div class="phase"><div class="phase-head"><span class="num">1</span><div><h3>Rendez-vous découverte</h3><p class="meta-line"><span class="free">{ic("clock")}Offert · 30 min</span><span>{ic("video")}En visio</span><span>{ic("pin")}ou en présentiel</span></p></div></div>
<div class="vsb">{v}</div><p class="phase-note">{note}</p></div>'''

def flow(label):
    return f'<div class="flow">{ic("down")}<span>{label}</span></div>'

def rpbdc(items):
    return '<dl class="rpbdc">' + "".join(f'<div><dt><span>{k[0]}</span>{k[2:]}</dt><dd>{v}</dd></div>' for k,v in items) + '</dl>'

def arrows(items):
    return '<ul class="arrows">' + "".join(f'<li>{ic("arrow")}{i}</li>' for i in items) + '</ul>'

def tags(items, accent=False):
    return f'<div class="tags{" accent" if accent else ""}">' + "".join(f'<span>{i}</span>' for i in items) + '</div>'

def duo(a, a_sub, mid, b, b_sub, a_ic="usercheck", b_ic="target"):
    return f'<div class="duo"><div class="who">{ic(a_ic)}<b>{a}</b><span>{a_sub}</span></div><div class="mid">{ic("lr")}<span>{mid}</span></div><div class="who">{ic(b_ic)}<b>{b}</b><span>{b_sub}</span></div></div>'

def crumbs(items):
    out = '<nav class="crumbs" aria-label="Fil d’Ariane"><a href="/">Accueil</a>'
    for i,(label,url) in enumerate(items):
        out += '<span aria-hidden="true">›</span>'
        out += f'<a href="{url}">{label}</a>' if url else (f'<span>{label}</span>' if url == "" else f'<span aria-current="page">{label}</span>')
    return out + '</nav>'

def offer_hero(trail, img, kicker, h1, tagline, lead, toc, how="concretement"):
    t = "".join(f'<li><a href="#{a}">{b}</a></li>' for a,b in toc)
    return f'''<section class="hero"><div class="wrap">
{crumbs(trail)}
<div class="offer-hero"><img class="art" src="{img}" alt="" width="200" height="200"><div class="txt"><p class="kicker gray">{kicker}</p><h1>{h1}</h1><p class="tagline">{tagline}</p><p class="lead">{lead}</p>
<div class="btns"><a class="btn" href="/contact/">Premier échange offert {ic("arrow")}</a><a class="btn ghost" href="#{how}">Comment ça se passe</a></div></div></div></div></section>
'''

def mini_offer(o):
    u,t,img,d = o
    return f'<a class="mini-offer" href="{u}"><img src="{img}" alt="" width="72" height="72"><span><b>{t}</b><span>{d}</span></span></a>'

def others(items, title="Voir aussi"):
    return sec("autres", '<div class="others">' + "".join(mini_offer(o) for o in items) + '</div>', cls="alt", h2=title)

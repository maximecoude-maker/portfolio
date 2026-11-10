# -*- coding: utf-8 -*-
"""Générateur du portfolio statique — python3 build.py"""
import os, re, html
from data_fr import LANDING_FR, PROJECTS_FR, CASE_LABELS_FR
from data_en import LANDING_EN, PROJECTS_EN, CASE_LABELS_EN

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://maximecoude.com/"          # domaine canonique
OG_IMAGE = BASE + "assets/img/og-cover.jpg"  # aperçu de partage (jpg, non réécrit en webp)

# Verrou de refonte. True = toutes les routes publiques sont renvoyees vers
# maintenance.html via vercel.json, et robots.txt interdit l'exploration.
# Repasser a False puis rebuild pour rouvrir le site.
MAINTENANCE = True

# Toutes les images raster sont servies en .webp (générées à part, PNG conservés en source).
# On réécrit les références .png -> .webp au moment d'écrire la page (bijection 1:1).
_PNG_REF = re.compile(r'((?:\.\./)*assets/img/[\w\-./]+?)\.png')

def write_page(path, page):
    page = _PNG_REF.sub(lambda m: m.group(0) if '/cats/' in m.group(1) else m.group(1) + '.webp', page)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)

SOCIAL_LINKS = [
    ("https://www.linkedin.com/in/maximecoude", "LinkedIn", "icon-linkedin.png", "_blank"),
    ("https://wa.me/33675434488", "WhatsApp", "icon-whatsapp.png", "_blank"),
    ("mailto:maxime.coude@gmail.com", "Envoyez-moi un message", "icon-message.png", ""),
]

def socials_html(rel):
    out = ""
    for href, label, icon, target in SOCIAL_LINKS:
        t = f' target="{target}" rel="noopener"' if target else ""
        out += (f'<a href="{href}" aria-label="{label}"{t}>'
                f'<img src="{rel}assets/img/{icon}" alt="{label}"></a>\n')
    return out

def head(title, css_rel, lang, description, canonical, alternates, og_type="website",
         noindex=False):
    desc = html.escape(description, quote=True)
    robots = '\n<meta name="robots" content="noindex, nofollow">' if noindex else ""
    alts = "".join(
        f'\n<link rel="alternate" hreflang="{hl}" href="{href}">' for hl, href in alternates)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">{alts}{robots}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Maxime Coudé">
<meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_US'}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title, quote=True)}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{css_rel}assets/fonts/gilroy-extrabold.woff2">
<link rel="stylesheet" href="{css_rel}assets/css/style.css?v=20261107ca">
<link rel="icon" type="image/png" href="{css_rel}assets/img/icon-notes.png">
</head>
<body>"""

def nav(L, rel, lang_href, home_href):
    n = L["nav"]
    middle_link = (f'<a href="https://www.linkedin.com/in/maxime-coude-3a493865/" target="_blank" rel="noopener">{n["linkedin"]}</a>'
                   if n.get("linkedin") else f'<a href="{home_href}#apropos">{n["about"]}</a>')
    return f"""
<header class="nav-wrap">
  <nav class="nav">
    <a class="nav-cta" href="{home_href}">{n['name']}</a>
    <button class="nav-burger" aria-label="Menu" aria-expanded="false" aria-controls="nav-links">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-links" id="nav-links">
      <a href="{home_href}#projets">{n['projects']}</a>
      {middle_link}
      <a href="{home_href}#contact">{n['contact']}</a>
      <a class="nav-lang" href="{lang_href}">{L['other_lang_label']}</a>
    </div>
  </nav>
</header>"""

def contact(L, rel):
    return f"""
<section class="contact" id="contact">
  <div class="contact-inner">
    <h2 class="reveal">{L['contact_h2']}</h2>
    <div class="socials reveal">{socials_html(rel)}</div>
    <p class="coords reveal">{L['contact_coords']}</p>
  </div>
  <img class="avatar-corner" src="{rel}assets/img/avatar-contact.png" alt="" data-ph="avatar 3D (contact)">
</section>
<script src="{rel}assets/js/main.js"></script>
</body>
</html>"""

def devices_html(rel, devices, panel=None, caption=None, extra_class=""):
    """Grille de cadres mobiles. Réservé aux vraies captures d'écrans mobiles :
    les captures web passent par img_or_ph, jamais par un device frame."""
    cells = "".join(
        f'<div class="device"><img src="{rel}assets/img/{src}" '
        f'alt="{html.escape(alt)}" loading="lazy"></div>'
        for src, alt in devices)
    style = f' style="background:{panel}"' if panel else ""
    cap = f"<figcaption>{html.escape(caption)}</figcaption>" if caption else ""
    cls = ("device-gallery " + extra_class).strip()
    return f'<figure class="fig {cls}"><div class="device-row"{style}>{cells}</div>{cap}</figure>'

def img_or_ph(rel, img, tall=True):
    if not img: return ""
    if isinstance(img, dict):
        return devices_html(rel, img["devices"], img.get("panel"), img.get("caption"))
    src, alt = img
    t = ' data-tall="true"' if tall else ''
    return f'<figure class="fig"><img src="{rel}assets/img/{src}" alt="{html.escape(alt)}" data-ph="{html.escape(alt)} — exporter depuis Figma : {src}"{t} loading="lazy"><figcaption>{html.escape(alt)}</figcaption></figure>'

# Icônes toolkit (assets transparents à la racine assets/img/)
TOOL_ICONS = {
    "Miro": "miro", "Figma": "Figma", "Interview": "Interview",
    "Card sorting": "CardSorting", "Survey": "Survey", "Board": "Notes",
    "Sketch": "sketch", "Zeplin": "zepplin", "After Effects": "Aftereffect",
    "ZeroHeight": "Zeroheight", "Maze": "maze", "Eye Tracking": "Eyetracking",
    "Illustrator": "illlustrator",
}

def chip_html(rel, t):
    icon = TOOL_ICONS.get(t)
    icon_tag = f'<img src="{rel}assets/img/{icon}.png" alt="" class="chip-icon" loading="lazy">' if icon else ""
    return f'<span class="chip">{icon_tag}{html.escape(t)}</span>'

# Photos de remerciements : convention people/<slug>.png (sans accents ni espaces)
def people_slug(n):
    import unicodedata
    s = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode().lower()
    return "-".join(s.split())

def brand_html(rel, p, logo=None, logo_alt=None):
    logo = logo or p.get("brand_logo")
    esc = html.escape(p["brand"])
    if not logo:
        return f'<span class="brand">{esc}</span>'
    imgs = (f'<img class="brand-logo brand-logo-main" src="{rel}assets/img/{logo}" '
            f'alt="{esc}" onerror="this.parentNode.textContent=this.alt">')
    if logo_alt:
        imgs += f'<img class="brand-logo brand-logo-alt" src="{rel}assets/img/{logo_alt}" alt="{esc}">'
    return f'<span class="brand">{imgs}</span>'

def person_html(rel, accent, n):
    slug = people_slug(n)
    initials = "".join(w[0] for w in n.split()[:2]).upper()
    esc = html.escape(n)
    photo = os.path.join(ROOT, "assets", "img", "people", f"{slug}.png")
    if os.path.exists(photo):
        avatar = f'<img class="pp" src="{rel}assets/img/people/{slug}.png" alt="{esc}" loading="lazy">'
    else:
        avatar = f'<span class="pp" style="background:{accent}">{html.escape(initials)}</span>'
    return f'<div class="person">{avatar}{esc}</div>'

# ------------------------------------------------------------------
def build_landing(L, projects, out_path, rel, lang_href, proj_dir, canonical, alternates):
    cards = ""
    for p in projects:
        if p.get("hidden"):
            continue
        card_img = p.get("card_img", p["slug"] + "-thumb.png")
        bg = p["hero_bg"]
        # La carte peut avoir des couleurs de texte propres (fond visuel) indépendantes du hero
        fg = p.get("card_fg", p["hero_fg"])
        title_color = p.get("card_title_color", p.get("hero_title_color"))
        btn = "btn-light" if fg == "#FFFFFF" else "btn-dark"
        title_html = p.get("card_title_html") or p.get("hero_title_html") or html.escape(p['hero_title'])
        title_style = f' style="color:{title_color}"' if title_color else ""
        cta_var = f"--cta:{p['card_cta_color']};" if p.get("card_cta_color") else ""
        content = (f'<div class="card-content">\n'
                   f'        {brand_html(rel, p, p.get("card_brand_logo"), p.get("card_brand_logo_alt"))}\n'
                   f'        <h3{title_style}>{title_html}</h3>\n'
                   f'        <p>{html.escape(p["hero_desc"])}</p>\n'
                   f'        <span class="btn {btn}">{L["see_project"]} →</span>\n'
                   f'      </div>')
        if p.get("card_variant") == "split-visual-left":
            bg_color = p.get("card_bg_color", bg)
            style = f"background:{bg_color};{cta_var}color:{fg};"
            cards += f"""
    <a class="project-card card-split-left card-{p['slug']} reveal" href="{proj_dir}{p['slug']}.html" style="{style}">
      <div class="card-visual">
        <img src="{rel}assets/img/{card_img}" alt="" data-ph="visuel carte {html.escape(p['name'])} ({card_img})">
      </div>
      {content}
    </a>"""
        elif p.get("card_bg"):
            align = p.get("card_text", "left")
            pos = {"left": "right", "right": "left", "center": "center"}[align]
            bg_color = p.get("card_bg_color", bg)
            thumb_url = f"url('{rel}assets/img/{card_img}')"
            if bg_color.startswith("linear-gradient"):
                # thumb superposé au dégradé (les 2 sont des background-image)
                bg_decl = (f"background-image:{thumb_url}, {bg_color};"
                           f"background-size:cover, cover;background-repeat:no-repeat;"
                           f"background-position:{pos} center, center;")
            else:
                bg_decl = (f"background-color:{bg_color};background-image:{thumb_url};"
                           f"background-size:cover;background-repeat:no-repeat;background-position:{pos} center;")
            style = f"--card-bg:{bg_color};{cta_var}color:{fg};{bg_decl}"
            cards += f"""
    <a class="project-card card-bg card-{p['slug']} text-{align} reveal" href="{proj_dir}{p['slug']}.html" style="{style}">
      {content}
    </a>"""
        else:
            style = f"background:{bg};{cta_var}color:{fg};"
            cards += f"""
    <a class="project-card card-{p['slug']} reveal" href="{proj_dir}{p['slug']}.html" style="{style}">
      {content}
      <div class="card-visual">
        <img src="{rel}assets/img/{card_img}" alt="" data-ph="visuel carte {html.escape(p['name'])} ({card_img})">
      </div>
    </a>"""

    offers = ""
    for i, (t, d) in enumerate(L["offers"], 1):
        offers += f"""
      <div class="offer reveal"><img class="offer-icon" src="{rel}assets/img/offers/offer-{i}.png" alt="" loading="lazy"><h4>{t}</h4><p>{d}</p></div>"""

    stats = "".join(f'<div class="stat"><div class="emoji">{e}</div><div class="label">{l}</div></div>' for e, l in L["stats"])
    bigstats = "".join(f'<div><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in L["big_stats"])
    import unicodedata
    def slug(c):
        s = unicodedata.normalize("NFKD", c).encode("ascii", "ignore").decode().lower()
        return "-".join(s.split())
    clients = "".join(f'<div class="client-logo" title="{c}"><img src="{rel}assets/img/logo-{slug(c)}.png" alt="{c}" onerror="this.replaceWith(Object.assign(document.createElement(\'span\'),{{textContent:\'{c}\'}}))"></div>' for c in L["clients"])

    page = head(L["title"], rel, L["lang"], L["meta_desc"], canonical, alternates)
    page += nav(L, rel, lang_href, "index.html" if rel == "" else "../index.html")
    page += f"""
<main>
  <section class="hero">
    <h1>{L['hero_h1']}</h1>
    <p class="sub">{L['hero_sub']}</p>
    <img class="avatar" src="{rel}assets/img/avatar.png" alt="Avatar 3D de Maxime" data-ph="avatar 3D du hero (avatar.png)" data-tall="true">
  </section>

  <div class="landing-body">
  <section class="about" id="apropos">
    <div class="container">
      <div class="about-grid">
        <div class="reveal about-intro">
          <div class="quote-block">
            <div class="quote-mark">“</div>
            <h3>{L['about_title']}</h3>
            <p>{L['about_text']}</p>
            <div class="quote-mark end">”</div>
          </div>
          <div class="about-stats">{stats}</div>
        </div>
        <div class="offers reveal">
          <h3 class="offers-title">{L['offers_title']}</h3>
          <div class="offers-grid">{offers}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="container" id="projets">
    <div class="projects">{cards}
      <div class="feedbacks-grid reveal">
        <div class="feedback-card purple">
          <h3>{L['feedback_title']}</h3>
          <p class="feedback-quote">{L['feedback_text']}</p>
          <div class="feedback-author">
            <img src="{rel}assets/img/people/damien-mordaque.png" alt="Damien Mordaque" loading="lazy">
            <span><strong>Damien Mordaque</strong><em>{L['feedback_author_role']}</em></span>
          </div>
        </div>
        <div class="feedback-card red"><div class="big-stats">{bigstats}</div></div>
      </div>
    </div>
  </section>
  </div>

  <section class="clients container">
    <h2 class="reveal">{L['clients_title']}</h2>
    <div class="clients-row reveal">{clients}</div>
  </section>
</main>"""
    page += contact(L, rel)
    write_page(out_path, page)

# ------------------------------------------------------------------
def build_case(p, L, LAB, out_path, rel, lang_href, home_href, next_proj, proj_dir, canonical, alternates):
    fg = p["hero_fg"]
    hero_bg_img_css = ""
    if p.get("hero_bg_img"):
        hero_bg_img_css = f"background-image:url('{rel}assets/img/{p['hero_bg_img']}');background-size:cover;background-position:bottom center;background-repeat:no-repeat;"
    challenges = ""
    for i, (t, d) in enumerate(p["challenges"], 1):
        desc = f"<p>{html.escape(d)}</p>" if d else ""
        challenges += f'<div class="challenge reveal"><div class="num" style="color:{p["accent"]}">{i}</div><h4>{html.escape(t)}</h4>{desc}</div>'
    two = " two" if len(p["challenges"]) <= 4 else ""

    tasks = "".join(f"<li>{html.escape(t)}</li>" for t in p["tasks"])
    tasks2 = ""
    if p["tasks2"]:
        items2 = "".join(f"<li>{html.escape(t)}</li>" for t in p["tasks2"])
        tasks2 = f'<h4 style="margin-top:32px">{LAB["tasks2"]}</h4><ul class="task-list secondary">{items2}</ul>'
    chips = "".join(chip_html(rel, t) for t in p["toolkit"])
    phases = "".join(f'<div class="phase">{html.escape(ph)}</div>' for ph in p["phases"])
    dpis = "".join(f"<span>{d}</span>" for d in LAB["dpis"])

    def paras(plist):
        out = ""
        for t in plist:
            if t == "__PROTO__": t = LAB["proto_note"]
            out += f"<p class='lead'>{html.escape(t)}</p>"
        return out

    research = ""
    for title, plist, img in p["research"]:
        research += f'<div class="sub-block reveal"><h3>{html.escape(title)}</h3>{paras(plist)}{img_or_ph(rel, img)}</div>'

    insights = ""
    if p["insights"]:
        cells = ""
        for i, (t, d) in enumerate(p["insights"], 1):
            cells += f'<div class="insight"><div class="num" style="color:{p["accent"]}">{i}</div><h4>{html.escape(t)}</h4><p>{html.escape(d)}</p></div>'
        insights = f'<div class="insights reveal">{cells}</div>'

    solution = ""
    for title, plist, img in p["solution"]:
        solution += f'<div class="sub-block reveal"><h3>{html.escape(title)}</h3>{paras(plist)}{img_or_ph(rel, img)}</div>'

    impacts = ""
    if p["impacts"]:
        cells = "".join(f'<div class="impact"><div class="v">{html.escape(v)}</div><div class="l">{html.escape(l)}</div></div>' for v, l in p["impacts"])
        intro = f"<p class='lead'>{html.escape(p['impacts_text'])}</p>" if p["impacts_text"] else ""
        impacts = f"""
  <section class="case-section container">
    <h2 class="reveal">{LAB['impacts']}</h2>
    {intro}
    <div class="impacts-grid reveal">{cells}</div>
  </section>"""

    thanks = ""
    for title, names in p["thanks"]:
        people = "".join(person_html(rel, p["accent"], n) for n in names)
        thanks += f'<div class="thanks-group reveal"><h4>{html.escape(title)}</h4><div class="people">{people}</div></div>'

    if p.get("hero_devices"):
        hero_visual = devices_html(rel, p["hero_devices"], extra_class="hero-devices")
    else:
        hero_visual = (f'<img src="{rel}assets/img/{p["hero_img"][0]}" '
                       f'alt="{html.escape(p["hero_img"][1])}" '
                       f'data-ph="{html.escape(p["hero_img"][1])} ({p["hero_img"][0]})" '
                       f'data-tall="true">')

    title_html = p.get("hero_title_html") or html.escape(p["hero_title"])
    title_style = f' style="color:{p["hero_title_color"]}"' if p.get("hero_title_color") else ""
    align_cls = f' align-{p["hero_align"]}' if p.get("hero_align") else ""
    split_cls = ' hero-split' if p.get("hero_split") else ""

    intro = html.unescape(re.sub("<[^>]+>", " ", p["hero_desc"]))
    if L["lang"] == "fr":
        case_desc = f"{p['name']} · étude de cas Product Design UX/UI par Maxime Coudé. {intro}"
    else:
        case_desc = f"{p['name']} · Product Design UX/UI case study by Maxime Coudé. {intro}"
    case_desc = case_desc[:157].rstrip() + "…" if len(case_desc) > 158 else case_desc
    page = head(f"{p['name']} — {L['title']}", rel, L["lang"], case_desc, canonical, alternates,
                og_type="article", noindex=bool(p.get("hidden")))
    page += nav(L, rel, lang_href, home_href)
    page += f"""
<main>
  <section class="case-hero case-{p['slug']}{align_cls}{split_cls}" style="background:{p['hero_bg']};color:{fg};{hero_bg_img_css}">
    {brand_html(rel, p)}
    <h1{title_style}>{title_html}</h1>
    <p>{html.escape(p['hero_desc'])}</p>
    <div class="hero-visual">
      {f'<img class="hero-shadow" src="{rel}assets/img/{p["hero_shadow_img"]}" alt="" aria-hidden="true">' if p.get('hero_shadow_img') else ''}
      {hero_visual}
    </div>
  </section>

  <section class="case-section container">
    <h2 class="reveal">{LAB['mission']}</h2>
    <div class="reveal">{paras(p['mission'])}</div>
    {img_or_ph(rel, p.get('mission_img'))}
    <div class="challenges{two}">{challenges}</div>
  </section>

  <section class="case-section tight container">
    <h2 class="reveal">{LAB['role']}</h2>
    <div class="role-grid">
      <div class="reveal">{paras(p['role'])}</div>
      <div class="reveal">
        <h4>{LAB['tasks']}</h4><ul class="task-list">{tasks}</ul>
        {tasks2}
        <div class="toolkit" style="margin-top:40px"><h4>{LAB['toolkit']}</h4><div class="toolkit-chips">{chips}</div></div>
      </div>
    </div>
  </section>

  <section class="case-section tight container">
    <h2 class="reveal">{LAB['planning']}</h2>
    <p class="lead reveal">{html.escape(p['planning_text'])}</p>
    <div class="phases reveal">{phases}</div>
    {img_or_ph(rel, p.get('planning_img'))}
    <div class="dpis reveal">{dpis}</div>
  </section>
"""
    if p["research"] or p["insights"]:
        page += f"""
  <section class="case-section tight container">
    <h2 class="reveal">{LAB['research']}</h2>
    {research}
    {insights}
  </section>"""
    page += f"""
  <section class="case-section tight container">
    <h2 class="reveal">{LAB['solution']}</h2>
    {solution}
  </section>
{impacts}
  <section class="case-section tight container">
    <h2 class="reveal">{LAB['thanks']}</h2>
    {thanks}
  </section>

  <div class="container case-footer-nav">
    <a href="{home_href}#projets">{LAB['back']}</a>
    <a href="{next_proj}">{LAB['next']}</a>
  </div>
</main>"""
    page += contact(L, rel)
    write_page(out_path, page)

# ------------------------------------------------------------------
def clean_url(path):
    """URL absolue canonique : on retire index.html final."""
    return BASE + re.sub(r'(^|/)index\.html$', r'\1', path)

MAINTENANCE_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Maxime Coudé — Site en cours de refonte</title>
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="Le portfolio de Maxime Coudé, Senior Product Designer UX/UI freelance, est en cours de refonte. Contact par e-mail ou LinkedIn.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="/assets/img/icon-notes.png">
<style>
:root{--blue:#4975E9;--black:#0A0A0A;--grey:#6E6E78;--grey-1:#F7F7F9}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{min-height:100vh;display:flex;align-items:center;justify-content:center;
  padding:40px 24px;background:var(--grey-1);color:var(--black);
  font-family:'Montserrat',system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{width:100%;max-width:560px;text-align:center}
.badge{display:inline-flex;align-items:center;gap:8px;padding:8px 16px;margin-bottom:28px;
  border-radius:999px;background:#fff;border:1px solid #E4E4EC;
  font-size:13px;font-weight:600;letter-spacing:.01em;color:var(--grey)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--blue)}
h1{margin:0 0 20px;font-size:clamp(28px,5.4vw,40px);line-height:1.18;font-weight:800;letter-spacing:-.02em}
p{margin:0 auto 14px;max-width:44ch;font-size:clamp(15px,2.2vw,17px);line-height:1.6;color:var(--grey);font-weight:500}
.en{margin-top:22px;padding-top:22px;border-top:1px solid #E4E4EC;font-size:14px}
.actions{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:34px}
a.btn{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 26px;
  border-radius:999px;font-size:15px;font-weight:700;text-decoration:none;transition:opacity .2s}
a.primary{background:var(--blue);color:#fff}
a.secondary{background:#fff;color:var(--black);border:1px solid #E4E4EC}
a.btn:hover{opacity:.85}
a.btn:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
</head>
<body>
<main>
  <span class="badge"><span class="dot"></span>Refonte en cours</span>
  <h1>Le site fait peau neuve</h1>
  <p>Je retravaille la présentation de mon travail et de mes études de cas. Le portfolio sera de nouveau en ligne très prochainement.</p>
  <p>En attendant, mes projets et mes disponibilités restent accessibles sur demande.</p>
  <div class="actions">
    <a class="btn primary" href="mailto:maxime.coude@gmail.com">Me contacter</a>
    <a class="btn secondary" href="https://www.linkedin.com/in/maximecoude" target="_blank" rel="noopener">LinkedIn</a>
  </div>
  <p class="en"><strong>This portfolio is being redesigned.</strong><br>Maxime Coudé, Senior Product Designer UX/UI, freelance. Case studies available on request.</p>
</main>
</body>
</html>
"""

def build_maintenance():
    """Page d'attente servie a la place de tout le site quand MAINTENANCE est True."""
    with open(os.path.join(ROOT, "maintenance.html"), "w", encoding="utf-8") as f:
        f.write(MAINTENANCE_HTML)
    cfg = (
        '{\n'
        '  "rewrites": [\n'
        '    {\n'
        '      "source": "/((?!assets/|maintenance\\\\.html|robots\\\\.txt).*)",\n'
        '      "destination": "/maintenance.html"\n'
        '    }\n'
        '  ]\n'
        '}\n'
    )
    with open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8") as f:
        f.write(cfg)


def build_seo_files(urls):
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        if MAINTENANCE:
            f.write("User-agent: *\nDisallow: /\n")
        else:
            f.write("User-agent: *\nAllow: /\n\nSitemap: " + BASE + "sitemap.xml\n")
    items = "".join(
        f"\n  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>"
        for u, pr in urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                + items + "\n</urlset>\n")

def alts(fr_path, en_path):
    """Cluster hreflang partagé (fr + en + x-default) pour une paire de pages."""
    fr, en = clean_url(fr_path), clean_url(en_path)
    return [("fr", fr), ("en", en), ("x-default", fr)]

def next_visible(projects, i):
    """Slug suivant dans la navigation de bas de page, en sautant les projets
    masques. Un projet masque renvoie vers le premier projet visible."""
    n = len(projects)
    for step in range(1, n + 1):
        nxt = projects[(i + step) % n]
        if not nxt.get("hidden"):
            return nxt["slug"] + ".html"
    return projects[i]["slug"] + ".html"

def build_all():
    sitemap = []
    projects_fr = list(PROJECTS_FR)
    projects_en = list(PROJECTS_EN)
    # Paires FR/EN (chemins relatifs à la racine du domaine)
    landing = ("index.html", "en/index.html")
    cases = [(f"projets/{p['slug']}.html", f"en/projects/{p['slug']}.html") for p in projects_fr]

    # FR
    a = alts(*landing)
    build_landing(LANDING_FR, projects_fr, os.path.join(ROOT, "index.html"),
                  rel="", lang_href="en/index.html", proj_dir="projets/",
                  canonical=clean_url(landing[0]), alternates=a)
    sitemap.append((clean_url(landing[0]), "1.0"))
    for i, p in enumerate(projects_fr):
        nxt = next_visible(projects_fr, i)
        fr_path, en_path = cases[i]
        build_case(p, LANDING_FR, CASE_LABELS_FR,
                   os.path.join(ROOT, "projets", p["slug"] + ".html"),
                   rel="../", lang_href=f"../en/projects/{p['slug']}.html",
                   home_href="../index.html", next_proj=nxt, proj_dir="",
                   canonical=clean_url(fr_path), alternates=alts(fr_path, en_path))
        if not p.get("hidden"):
            sitemap.append((clean_url(fr_path), "0.8"))
    # EN
    build_landing(LANDING_EN, projects_en, os.path.join(ROOT, "en", "index.html"),
                  rel="../", lang_href="../index.html", proj_dir="projects/",
                  canonical=clean_url(landing[1]), alternates=a)
    sitemap.append((clean_url(landing[1]), "0.9"))
    for i, p in enumerate(projects_en):
        nxt = next_visible(projects_en, i)
        fr_path, en_path = cases[i]
        build_case(p, LANDING_EN, CASE_LABELS_EN,
                   os.path.join(ROOT, "en", "projects", p["slug"] + ".html"),
                   rel="../../", lang_href=f"../../projets/{p['slug']}.html",
                   home_href="../index.html", next_proj=nxt, proj_dir="",
                   canonical=clean_url(en_path), alternates=alts(fr_path, en_path))
        if not p.get("hidden"):
            sitemap.append((clean_url(en_path), "0.7"))

    build_seo_files(sitemap)
    if MAINTENANCE:
        build_maintenance()
    print(f"{len(projects_fr) + len(projects_en) + 2} pages générées + robots.txt + sitemap.xml")

if __name__ == "__main__":
    build_all()

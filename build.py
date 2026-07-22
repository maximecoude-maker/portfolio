# -*- coding: utf-8 -*-
"""Générateur du portfolio statique — python3 build.py"""
import os, html
from data_fr import LANDING_FR, PROJECTS_FR, CASE_LABELS_FR
from data_en import LANDING_EN, PROJECTS_EN, CASE_LABELS_EN

ROOT = os.path.dirname(os.path.abspath(__file__))

SOCIALS = """
<a href="https://www.linkedin.com/in/maximecoude" aria-label="LinkedIn" target="_blank" rel="noopener">
  <svg viewBox="0 0 24 24"><path d="M4 4h4v16H4zM6 2a2 2 0 1 1 0 .01M10 9h4v2c.8-1.4 2.2-2.3 4-2.3 3 0 4 2 4 5V20h-4v-5.5c0-1.5-.5-2.5-2-2.5s-2 1-2 2.5V20h-4z"/></svg></a>
<a href="https://join.slack.com" aria-label="Slack" target="_blank" rel="noopener">
  <svg viewBox="0 0 24 24"><path d="M9 3a2 2 0 1 0 0 4h2V5a2 2 0 0 0-2-2zM15 21a2 2 0 1 0 0-4h-2v2a2 2 0 0 0 2 2zM3 15a2 2 0 1 0 4 0v-2H5a2 2 0 0 0-2 2zM21 9a2 2 0 1 0-4 0v2h2a2 2 0 0 0 2-2zM9 9h6v6H9z"/></svg></a>
<a href="https://wa.me/33675434488" aria-label="WhatsApp" target="_blank" rel="noopener">
  <svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z"/><path d="M8.5 9.5c.5 2.5 3.5 5.5 6 6l1.5-1.5-2-1.5-1 .8c-1-.5-2.3-1.8-2.8-2.8l.8-1-1.5-2z"/></svg></a>
<a href="mailto:maxime.coude@gmail.com" aria-label="Email">
  <svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></a>
"""

def head(title, css_rel, lang):
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="Maxime COUDE — Product Designer UX/UI Freelance">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_rel}assets/css/style.css">
<link rel="icon" type="image/png" href="{css_rel}assets/img/icon-notes.png">
</head>
<body>"""

def nav(L, rel, lang_href, home_href):
    n = L["nav"]
    return f"""
<header class="nav-wrap">
  <nav class="nav">
    <a class="nav-cta" href="{home_href}">{n['name']}</a>
    <a href="{home_href}#projets">{n['projects']}</a>
    <a href="{home_href}#apropos">{n['about']}</a>
    <a href="{home_href}#contact">{n['contact']}</a>
    <a class="nav-lang" href="{lang_href}">{L['other_lang_label']}</a>
  </nav>
</header>"""

def contact(L, rel):
    return f"""
<section class="contact" id="contact">
  <div class="contact-inner">
    <h2 class="reveal">{L['contact_h2']}</h2>
    <div class="socials reveal">{SOCIALS}</div>
    <p class="coords reveal">{L['contact_coords']}</p>
  </div>
  <img class="avatar-corner" src="{rel}assets/img/avatar-contact.png" alt="" data-ph="avatar 3D (contact)">
</section>
<script src="{rel}assets/js/main.js"></script>
</body>
</html>"""

def img_or_ph(rel, img, tall=True):
    if not img: return ""
    src, alt = img
    t = ' data-tall="true"' if tall else ''
    return f'<figure class="fig"><img src="{rel}assets/img/{src}" alt="{html.escape(alt)}" data-ph="{html.escape(alt)} — exporter depuis Figma : {src}"{t} loading="lazy"><figcaption>{html.escape(alt)}</figcaption></figure>'

# Icônes toolkit disponibles dans assets/img/icons/
TOOL_ICONS = {
    "Miro": "miro", "Figma": "figma", "Interview": "interview",
    "Card sorting": "card-sorting", "Survey": "survey", "Board": "board",
    "Sketch": "sketch", "Zeplin": "zeplin", "After Effects": "after-effects",
}

def chip_html(rel, t):
    icon = TOOL_ICONS.get(t)
    icon_tag = f'<img src="{rel}assets/img/icons/{icon}.png" alt="" class="chip-icon" loading="lazy">' if icon else ""
    return f'<span class="chip">{icon_tag}{html.escape(t)}</span>'

# Photos d'équipe disponibles dans assets/img/people/
PEOPLE_PHOTOS = {
    "Damien Mordaque": "damien-mordaque",
    "Kevin Mouzet": "kevin-mouzet",
    "Emile Leenhardt": "emile-leenhardt",
}

def person_html(rel, accent, n):
    slug = PEOPLE_PHOTOS.get(n)
    if slug:
        avatar = f'<img class="pp" src="{rel}assets/img/people/{slug}.png" alt="{html.escape(n)}" loading="lazy">'
    else:
        initials = "".join(w[0] for w in n.split()[:2]).upper()
        avatar = f'<span class="pp" style="background:{accent}">{html.escape(initials)}</span>'
    return f'<div class="person">{avatar}{html.escape(n)}</div>'

# ------------------------------------------------------------------
def build_landing(L, projects, out_path, rel, lang_href, proj_dir):
    cards = ""
    for p in projects:
        fg = p["hero_fg"]
        bg = p["hero_bg"]
        style = f"background:{bg};color:{fg};"
        btn = "btn-light" if fg == "#FFFFFF" else "btn-dark"
        title_html = p.get("hero_title_html") or html.escape(p['hero_title'])
        title_style = f' style="color:{p["hero_title_color"]}"' if p.get("hero_title_color") else ""
        cards += f"""
    <a class="project-card reveal" href="{proj_dir}{p['slug']}.html" style="{style}">
      <div class="card-content">
        <span class="brand">{html.escape(p['brand'])}</span>
        <h3{title_style}>{title_html}</h3>
        <p>{html.escape(p['hero_desc'])}</p>
        <span class="btn {btn}">{L['see_project']} →</span>
      </div>
      <div class="card-visual">
        <img src="{rel}assets/img/{p['slug']}-thumb.png" alt="" data-ph="visuel carte {html.escape(p['name'])} ({p['slug']}-thumb.png)">
      </div>
    </a>"""

    offers = ""
    for i, (t, d) in enumerate(L["offers"], 1):
        offers += f"""
      <div class="offer reveal"><div class="num">{i}</div><h4>{t}</h4><p>{d}</p></div>"""

    stats = "".join(f'<div class="stat"><div class="emoji">{e}</div><div class="label">{l}</div></div>' for e, l in L["stats"])
    bigstats = "".join(f'<div><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in L["big_stats"])
    import unicodedata
    def slug(c):
        s = unicodedata.normalize("NFKD", c).encode("ascii", "ignore").decode().lower()
        return "-".join(s.split())
    clients = "".join(f'<div class="client-logo" title="{c}"><img src="{rel}assets/img/logo-{slug(c)}.png" alt="{c}" onerror="this.replaceWith(Object.assign(document.createElement(\'span\'),{{textContent:\'{c}\'}}))"></div>' for c in L["clients"])

    page = head(L["title"], rel, L["lang"])
    page += nav(L, rel, lang_href, "index.html" if rel == "" else "../index.html")
    page += f"""
<main>
  <section class="hero">
    <h1>{L['hero_h1']}</h1>
    <p class="sub">{L['hero_sub']}</p>
    <img class="avatar" src="{rel}assets/img/avatar-hero.png" alt="Avatar 3D de Maxime" data-ph="avatar 3D du hero (avatar-hero.png)" data-tall="true">
  </section>

  <section class="about container" id="apropos">
    <div class="about-grid">
      <div class="reveal">
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
  </section>

  <section class="container" id="projets">
    <div class="projects">{cards}
      <div class="feedbacks-grid reveal">
        <div class="feedback-card purple">
          <h3>{L['feedback_title']}</h3>
          <p class="feedback-quote">{L['feedback_text']}</p>
        </div>
        <div class="feedback-card red"><div class="big-stats">{bigstats}</div></div>
      </div>
    </div>
  </section>

  <section class="clients container">
    <h2 class="reveal">{L['clients_title']}</h2>
    <div class="clients-row reveal">{clients}</div>
  </section>
</main>"""
    page += contact(L, rel)
    with open(out_path, "w", encoding="utf-8") as f: f.write(page)

# ------------------------------------------------------------------
def build_case(p, L, LAB, out_path, rel, lang_href, home_href, next_proj, proj_dir):
    fg = p["hero_fg"]
    btnstyle = f"color:{p['accent']}"
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
        cells = "".join(f'<div class="impact"><div class="v" style="color:{p["accent"]}">{html.escape(v)}</div><div class="l">{html.escape(l)}</div></div>' for v, l in p["impacts"])
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

    title_html = p.get("hero_title_html") or html.escape(p["hero_title"])
    title_style = f' style="color:{p["hero_title_color"]}"' if p.get("hero_title_color") else ""

    page = head(f"{p['name']} — {L['title']}", rel, L["lang"])
    page += nav(L, rel, lang_href, home_href)
    page += f"""
<main>
  <section class="case-hero" style="background:{p['hero_bg']};color:{fg};{hero_bg_img_css}">
    <span class="brand">{html.escape(p['brand'])}</span>
    <h1{title_style}>{title_html}</h1>
    <p>{html.escape(p['hero_desc'])}</p>
    <div class="hero-visual">
      {f'<img class="hero-shadow" src="{rel}assets/img/{p["hero_shadow_img"]}" alt="" aria-hidden="true">' if p.get('hero_shadow_img') else ''}
      <img src="{rel}assets/img/{p['hero_img'][0]}" alt="{html.escape(p['hero_img'][1])}" data-ph="{html.escape(p['hero_img'][1])} ({p['hero_img'][0]})" data-tall="true">
    </div>
  </section>

  <section class="case-section container">
    <h2 class="reveal">{LAB['mission']}</h2>
    <div class="reveal">{paras(p['mission'])}</div>
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
    <a href="{home_href}#projets" style="{btnstyle}">{LAB['back']}</a>
    <a href="{next_proj}" style="{btnstyle}">{LAB['next']}</a>
  </div>
</main>"""
    page += contact(L, rel)
    with open(out_path, "w", encoding="utf-8") as f: f.write(page)

# ------------------------------------------------------------------
def build_all():
    # FR
    build_landing(LANDING_FR, PROJECTS_FR, os.path.join(ROOT, "index.html"),
                  rel="", lang_href="en/index.html", proj_dir="projets/")
    for i, p in enumerate(PROJECTS_FR):
        nxt = PROJECTS_FR[(i + 1) % len(PROJECTS_FR)]["slug"] + ".html"
        build_case(p, LANDING_FR, CASE_LABELS_FR,
                   os.path.join(ROOT, "projets", p["slug"] + ".html"),
                   rel="../", lang_href=f"../en/projects/{p['slug']}.html",
                   home_href="../index.html", next_proj=nxt, proj_dir="")
    # EN
    build_landing(LANDING_EN, PROJECTS_EN, os.path.join(ROOT, "en", "index.html"),
                  rel="../", lang_href="../index.html", proj_dir="projects/")
    for i, p in enumerate(PROJECTS_EN):
        nxt = PROJECTS_EN[(i + 1) % len(PROJECTS_EN)]["slug"] + ".html"
        build_case(p, LANDING_EN, CASE_LABELS_EN,
                   os.path.join(ROOT, "en", "projects", p["slug"] + ".html"),
                   rel="../../", lang_href=f"../../projets/{p['slug']}.html",
                   home_href="../index.html", next_proj=nxt, proj_dir="")
    print("✔ 14 pages générées")

if __name__ == "__main__":
    build_all()

"""Case study CATS, composed with the portfolio's shared shell.

Content remains in data_fr.py / data_en.py. Evidence is sourced separately;
diagrams are labelled so they cannot be mistaken for product screenshots.
"""
from html import escape
from pathlib import Path
import struct


def image_dimensions(path):
    """Read dimensions of reviewed PNG/WebP assets with the standard library."""
    data = path.read_bytes()
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return struct.unpack('>II', data[16:24])
    if data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        chunk, payload = data[12:16], data[20:]
        if chunk == b'VP8X':
            return int.from_bytes(payload[4:7], 'little') + 1, int.from_bytes(payload[7:10], 'little') + 1
        if chunk == b'VP8 ':
            w, h = struct.unpack('<HH', payload[6:10])
            return w & 0x3fff, h & 0x3fff
        if chunk == b'VP8L':
            bits = int.from_bytes(payload[1:5], 'little')
            return (bits & 0x3fff) + 1, ((bits >> 14) & 0x3fff) + 1
    return None


def cats_project(content, lang):
    return {
        "slug": "cats", "name": "CATS", "brand": "Crédit Agricole Technologies & Services",
        "accent": "#173F35", "hero_bg": "#EAF3EF", "hero_fg": "#173F35",
        "hero_title": content["hero_title"], "hero_desc": content["hero_desc"],
        "card_img": f"cats-system-{lang}.svg",
        "hero_img": (f"cats-system-{lang}.svg", "NPC · Ma Banque · PUC"),
        "content": content,
    }


def build_cats(p, landing, rel, home_href, lang_href, canonical, alternates,
               root, head, nav, contact):
    c, lang = p["content"], landing["lang"]
    labels = c["labels"]
    fr = lang == "fr"

    def tr(french, english):
        return french if fr else english

    def e(value):
        return escape(str(value), quote=True)

    def section_head(number, label, title=None, intro=None):
        kicker = f'{number} / {label}' if number else label
        return (f'<header class="cats-section-head"><p class="cats-kicker">{e(kicker)}</p>'
                f'<h2>{e(title or label)}</h2>'
                + (f'<p class="cats-lead">{e(intro)}</p>' if intro else "") + '</header>')

    def evidence(key, title, caption, required=False, frame="plain"):
        # Only existing, reviewed assets are emitted. Missing evidence never
        # becomes a broken image or a reconstructed banking interface.
        source = None
        for folder in ("assets/img/cats", "public/cats"):
            for extension in ("webp", "png", "jpg"):
                candidate = f"{folder}/{key}.{extension}"
                if (Path(root) / candidate).is_file():
                    source = candidate
                    break
            if source:
                break
        if not source and not required:
            return ""
        figure_style = ""
        if source:
            dimensions = image_dimensions(Path(root) / source)
            size = f' width="{dimensions[0]}" height="{dimensions[1]}"' if dimensions else ''
            if dimensions and dimensions[0] < 600 and frame == "plain":
                figure_style = ' style="max-width:500px"'
            visual = (f'<a href="{rel}{e(source)}" target="_blank" rel="noopener" '
                      f'aria-label="{e(tr("Agrandir : ", "Enlarge: ") + title)}">'
                      f'<div class="cats-{e(frame)}"><img src="{rel}{e(source)}" '
                      f'alt="{e(title)}"{size} loading="lazy" decoding="async"></div></a>')
        else:
            visual = (f'<div class="cats-missing"><span>{e(labels["missing_visual"])}</span>'
                      f'<h4>{e(title)}</h4><p>{e(tr("Emplacement pour la capture d’origine.", "Space for the original screenshot."))}</p></div>')
        return (f'<figure class="cats-evidence"{figure_style}>{visual}<figcaption>'
                f'<strong>{e(title)}</strong> {e(caption)}</figcaption></figure>')

    def board(inside, caption):
        return (f'<figure class="cats-board"><p class="cats-board-label">{e(labels["diagram"])}</p>'
                f'{inside}<figcaption>{e(caption)}</figcaption></figure>')

    def decision_art(kind):
        if kind == "architecture":
            inside = f'''<div class="cats-map-card"><span>{e(tr("Le contexte", "Context"))}</span>
              <strong>{e(tr("La carte sélectionnée", "The selected card"))}</strong>
              <small>{e(tr("Titulaire · type · statut", "Cardholder · type · status"))}</small></div>
              <div class="cats-diagram-arrow" aria-hidden="true">↓</div>
              <div class="cats-map-actions"><span>{e(tr("Verrouiller", "Lock"))}</span>
              <span>{e(tr("Informations", "Details"))}</span><span>{e(tr("Plafonds", "Limits"))}</span></div>
              <div class="cats-diagram-arrow" aria-hidden="true">↓</div>
              <div class="cats-map-services">{e(tr("Paramètres & services", "Settings & services"))}</div>'''
            return board(inside, tr("Une hiérarchie commune, adaptable à chaque carte. Schéma de raisonnement, sans reproduction d’interface.",
                                     "A shared hierarchy that adapts to each card. Conceptual diagram, not a product interface."))
        if kind == "rules":
            rows = [
                (tr("Mineur · carte verrouillée", "Minor · locked card"),
                 tr("Seul votre parent peut la déverrouiller.", "Only your parent can unlock it."),
                 tr("Identifier qui peut agir", "Identify who can act")),
                (tr("Carte expirée", "Expired card"),
                 tr("Distinguer expiration et opposition", "Distinguish expiry from cancellation"),
                 tr("Éviter une fausse urgence", "Avoid a false sense of urgency")),
                (tr("Plusieurs cartes", "Multiple cards"),
                 tr("Rendre la carte sélectionnée explicite", "Make the selected card explicit"),
                 tr("Agir sur le bon support", "Act on the right card")),
            ]
            inside = '<div class="cats-rule-table"><table><thead><tr>'
            inside += ''.join(f'<th scope="col">{e(t)}</th>' for t in [tr("Situation", "Situation"), tr("Repère à donner", "Cue to provide")])
            inside += '</tr></thead><tbody>'
            inside += ''.join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}<small>{e(d)}</small></td></tr>' for a, b, d in rows)
            inside += '</tbody></table></div>'
            return board(inside, tr("Exemples de questions de conception. Les droits déterminent aussi l’explication et le relais nécessaires.",
                                     "Examples of design questions. Permissions also determine the explanation and support required."))
        if kind == "epin":
            steps = [("01", tr("L’intention", "Intent"), tr("Voir le code", "View PIN")),
                     ("02", tr("L’authentification", "Authentication"), "Securipass"),
                     ("03", tr("La consultation", "Viewing"), tr("Visuelle ou audio", "Visual or audio"))]
            inside = '<div class="cats-pin-flow">' + ''.join(f'<div><span>{n}</span><h4>{e(a)}</h4><p>{e(b)}</p></div>' for n, a, b in steps) + '</div>'
            inside += f'<p class="cats-takeaway">{e(tr("Code SMS ≠ code PIN. Une étape de sécurité doit expliquer son rôle.", "SMS code ≠ card PIN. Each security step needs a clear purpose."))}</p>'
            return board(inside, tr("Points d’attention du parcours testé : compréhension, accessibilité et confidentialité de la restitution.",
                                     "Focus of the tested journey: comprehension, accessibility and privacy when the PIN is presented."))
        inside = ''
        for title, score in [(tr("Facilité d’utilisation", "Ease of use"), "6,5"), (tr("Réponse au besoin", "Meets needs"), "4,7")]:
            percent = float(score.replace(',', '.')) / 7 * 100
            inside += (f'<div class="cats-trust-metric"><div class="cats-metric-heading"><span>{e(title)}</span>'
                       f'<strong>{e(score if fr else score.replace(",", "."))}<small>/7</small></strong></div>'
                       f'<div class="cats-bar" aria-hidden="true"><span style="--score:{percent:.2f}%"></span></div></div>')
        inside += f'<p class="cats-takeaway">{e(tr("Simple à utiliser ne veut pas toujours dire convaincant.", "Easy to use does not always mean convincing."))}</p>'
        return board(inside, tr("Card On File · TU3, novembre–décembre 2024. Deux items distincts, notes brutes sur 7.",
                                 "Card On File · TU3, November–December 2024. Two separate items, raw ratings out of 7."))

    meta = tr("Trois ans de Product Design UX/UI chez CATS : architecture Carte, gestion multicartes, recherche continue et continuité web, mobile et conseiller.",
              "Three years of Product Design at CATS: card experience architecture, multi-card management, continuous discovery and cross-channel consistency.")
    page = head(f"CATS — {landing['title']}", rel, lang, meta, canonical, alternates, og_type="article")
    page = page.replace('</head>', f'<link rel="stylesheet" href="{rel}assets/css/cats.css?v=20261028">\n</head>')
    page = page.replace('<body>', '<body class="cats-page">')
    page += f'<a class="cats-skip" href="#cats-main">{e(tr("Aller au contenu", "Skip to content"))}</a>'
    page += nav(landing, rel, lang_href, home_href)
    hero_visual = evidence("universe-mobile", "Ma Banque · Univers Carte",
                           tr("Extrait d’une maquette, capture d’octobre 2026. Données anonymisées ; écran complet au clic.",
                              "Design excerpt, captured in October 2026. Anonymised data; open for the full screen."), frame="device")
    if not hero_visual:
        hero_visual = (f'<img src="{rel}assets/img/cats-system-{lang}.svg" width="760" height="640" '
                       f'alt="{e(tr("Schéma : une carte relie NPC, Ma Banque et PUC.", "Diagram: one card connects NPC, Ma Banque and PUC."))}" fetchpriority="high">')
    else:
        hero_visual = hero_visual.replace('loading="lazy"', 'fetchpriority="high"')
    page += f'''<main id="cats-main" class="cats-case">
      <header class="cats-hero cats-wrap">
        <div class="cats-hero-copy"><p class="cats-eyebrow">{e(c['eyebrow'])}</p>
          <h1>{e(c['hero_title'])}</h1><p class="cats-lead">{e(c['hero_desc'])}</p>
          <p class="cats-period">{e(c['period'])}<br>{e(c['reading_time'])}</p>
          <a class="cats-read" href="#decisions">{e(tr("Comprendre mes choix", "Explore my decisions"))} <span aria-hidden="true">↓</span></a>
        </div>
        <div class="cats-hero-art">{hero_visual}</div>
      </header>
      <div class="cats-scale cats-wrap"><dl class="cats-scale-grid">'''
    page += ''.join(f'<div><dt>{e(s["value"])}</dt><dd>{e(s["label"])}</dd></div>' for s in c["scale"])
    page += f'</dl><p class="cats-note">{e(c["scale_note"])}</p></div>'
    sections = [("contexte", labels["context"]), ("decisions", tr("Les décisions", "Decisions")),
                ("recherche", tr("La recherche", "Research")), ("parcours", tr("Les parcours", "Journeys")),
                ("sprint", tr("Le sprint", "The sprint")), ("impact", tr("Les apports", "Contributions"))]
    page += f'<nav class="cats-toc" aria-label="{e(tr("Sommaire du projet", "Case study contents"))}">'
    page += ''.join(f'<a href="#{anchor}">{e(text)}</a>' for anchor, text in sections) + '</nav>'

    page += '<section class="cats-section cats-wrap" id="contexte">'
    page += section_head("01", labels["context"], c["intro_title"], c["intro"])
    page += '<div class="cats-scope">' + ''.join(f'<article><span>{e(s["tag"])}</span><h3>{e(s["name"])}</h3><p>{e(s["text"])}</p></article>' for s in c["scope"]) + '</div>'
    page += (f'<figure class="cats-system-map"><img src="{rel}assets/img/cats-system-{lang}.svg" width="760" height="640" '
             f'alt="{e(tr("Schéma de principe : une même carte, trois canaux, des contextes et des droits différents.", "Conceptual diagram: one card, three channels, different contexts and permissions."))}" loading="lazy"></figure>')
    page += f'<div class="cats-role"><p class="cats-kicker">{e(labels["role"])}</p><h3>{e(c["role_title"])}</h3><p>{e(c["role_intro"])}</p><div class="cats-role-list">'
    page += ''.join(f'<article><h4>{e(s["title"])}</h4><p>{e(s["text"])}</p></article>' for s in c["roles"]) + '</div></div>'
    page += '<div class="cats-principles">' + ''.join(f'<article><h3>{e(s["title"])}</h3><p>{e(s["text"])}</p></article>' for s in c["principles"]) + '</div></section>'

    page += '<section class="cats-section cats-wrap" id="decisions">'
    page += section_head("02", labels["decisions"], tr("Les choix derrière les écrans.", "The decisions behind the screens."), c["decision_intro"])
    for i, d in enumerate(c["decisions"], 1):
        page += f'<article class="cats-decision" id="decision-{e(d["id"])}"><div class="cats-decision-copy"><span class="cats-decision-index">{i:02d}</span><h3>{e(d["title"])}</h3><dl class="cats-reasoning">'
        for key in ("problem", "hypothesis", "decision", "learning"):
            page += f'<div><dt>{e(labels[key])}</dt><dd>{e(d[key])}</dd></div>'
        page += '</dl></div><div class="cats-decision-art">' + decision_art(d["visual"]) + '</div></article>'
        if d["visual"] == "architecture":
            page += '<div class="cats-comparison">'
            page += evidence("universe-before", tr("NPC · version 2023", "NPC · 2023 version"), tr("Structure verticale et accumulation de services. Écran de conception ; données personnelles masquées.", "Vertical structure and accumulated services. Design screen; personal details masked."), required=True, frame="browser")
            page += evidence("universe-after", tr("NPC · version 2026", "NPC · 2026 version"), tr("Carte sélectionnée, statut et hiérarchie des actions. Écran de conception ; données personnelles masquées.", "Selected card, status and action hierarchy. Design screen; personal details masked."), required=True, frame="browser") + '</div>'
            annotations = [
                (tr("Identifier", "Identify"), tr("Savoir à tout moment quelle carte est gérée.", "Always know which card is being managed.")),
                (tr("Agir", "Act"), tr("Distinguer les actions essentielles des services complémentaires.", "Distinguish essential actions from additional services.")),
                (tr("Faire évoluer", "Extend"), tr("Accueillir de nouveaux services sans allonger indéfiniment la page.", "Accommodate new services without continually extending the page.")),
            ]
            page += '<ol class="cats-annotations">' + ''.join(f'<li><span>{i:02d}</span><div><strong>{e(title)}</strong><p>{e(text)}</p></div></li>' for i, (title, text) in enumerate(annotations, 1)) + '</ol>'
            page += evidence("universe-detail", tr("Organiser les actions secondaires", "Organise secondary actions"), tr("NPC · dossier 2026. L’espace Paramètres prolonge la hiérarchie de gestion.", "NPC · 2026 source folder. Settings extend the management hierarchy."), frame="browser")
        if d["visual"] == "epin":
            group = ''.join(evidence(key, title, caption) for key, title, caption in [
                ("epin-choice", tr("Choisir la consultation", "Choose how to view"), tr("NPC · protocole TU5, janvier 2026. Rendre l’action explicite.", "NPC · TU5 protocol, January 2026. Make the action explicit.")),
                ("epin-visual", tr("Consulter son PIN", "View the card PIN"), tr("NPC · protocole TU5. Distinguer PIN et authentification.", "NPC · TU5 protocol. Distinguish PIN from authentication.")),
                ("epin-audio", tr("Prévoir la restitution audio", "Consider audio access"), tr("NPC · protocole TU5. Accessibilité et confidentialité.", "NPC · TU5 protocol. Accessibility and privacy."))])
            if group:
                page += f'<div class="cats-evidence-grid">{group}</div>'
        if d["visual"] == "trust":
            page += evidence("research-tu3", tr("La recherche en support", "Research as evidence"), tr("Extrait TU3 : comprendre l’acceptabilité du service au-delà de la fluidité du parcours.", "TU3 excerpt: understand the service’s acceptability beyond the ease of the journey."))
    page += '</section>'

    page += '<section class="cats-section cats-wrap" id="recherche">'
    page += section_head("03", labels["research"], tr("Tester pour décider. Puis retester.", "Test to decide. Then test again."), c["research_intro"])
    page += '<div class="cats-waves">'
    for wave in c["waves"]:
        page += f'<article class="cats-wave"><span class="cats-wave-id">{e(wave["id"])}</span><p class="cats-wave-date">{e(wave["date"])}</p><div class="cats-wave-content"><h3>{e(wave["title"])}</h3><p>{e(wave["text"])}</p><ul class="cats-wave-scores">'
        page += ''.join(f'<li><strong>{e(s["value"])}</strong> {e(s["label"])}</li>' for s in wave["scores"]) + '</ul></div></article>'
    page += f'</div><p class="cats-note">{e(c["research_note"])}</p></section>'

    page += '<section class="cats-section cats-wrap" id="parcours">'
    page += section_head("04", labels["stories"], tr("Un système, plusieurs situations de vie.", "One system, different moments in life."), c["stories_intro"])
    page += '<div class="cats-stories">' + ''.join(f'<article><h3>{e(s["title"])}</h3><p>{e(s["text"])}</p><p class="cats-takeaway">{e(s["learning"])}</p></article>' for s in c["stories"]) + '</div>'
    page += evidence("virtual-cards", tr("La carte virtuelle permanente", "The permanent virtual card"), tr("NPC · protocole TU5, janvier 2026. Parcours d’activation et présentation du service.", "NPC · TU5 protocol, January 2026. Activation journey and service presentation."))
    page += '<div class="cats-channel-section">' + section_head("", labels["channels"], intro=c["channels_intro"])
    page += '<div class="cats-channels">' + ''.join(f'<article><span>{e(s["audience"])}</span><h3>{e(s["name"])}</h3><p>{e(s["text"])}</p></article>' for s in c["channels"]) + '</div></div></section>'

    page += '<section class="cats-sprint" id="sprint"><div class="cats-wrap">'
    page += section_head("05", "Paiement Mobile / CA Pay", labels["sprint"], c["sprint_intro"])
    page += '<div class="cats-sprint-days">' + ''.join(f'<article><h3>{e(s["title"])}</h3><p>{e(s["text"])}</p></article>' for s in c["sprint_days"]) + '</div>'
    page += evidence("sprint-map", tr("Du cadrage aux tests", "From framing to testing"), tr("Organisation des ateliers et des trois journées du sprint. Mai 2026.", "Workshop schedule across the three days of the sprint. May 2026."))
    page += '<div class="cats-sprint-flow">' + ''.join(f'<span><b>{n:02d}</b>{e(text)}</span>' for n, text in enumerate([tr("Accéder depuis Ma Banque", "Enter from Ma Banque"), tr("Enrôler sa carte", "Enrol a card"), tr("Réaliser le premier paiement", "Make the first payment")], 1)) + '</div>'
    sprint_evidence = evidence("sprint-enrolment", tr("Un point d’entrée retravaillé", "A revised entry point"), tr("Itération du prototype après les tests. Mai 2026 ; état de conception.", "Prototype iteration after testing. May 2026; design material."))
    sprint_evidence += evidence("sprint-payment", tr("Un accès par widget", "Access through a widget"), tr("Exploration d’un accès direct depuis le widget Ma Banque. Prototype, mai 2026.", "Exploration of direct access through a Ma Banque widget. Prototype, May 2026."))
    if sprint_evidence:
        page += f'<div class="cats-comparison">{sprint_evidence}</div>'
    page += '<div class="cats-sprint-results">' + ''.join(f'<div><strong>{e(s["value"])}</strong><p>{e(s["text"])}</p></div>' for s in c["sprint_results"]) + '</div>'
    page += f'<p class="cats-lead">{e(c["sprint_learning"])}</p><p class="cats-note">{e(c["sprint_limit"])}</p>'
    page += evidence("sprint-research", tr("Ce que le panel a apprécié", "What participants appreciated"), tr("Extrait de restitution : accès, enrôlement et réassurance. Panel de quatre participants.", "Research summary excerpt: access, enrolment and reassurance. Four participants."))
    page += '</div></section>'

    page += '<section class="cats-section cats-wrap cats-system" id="muesli">'
    page += section_head("06", "Design System & " + tr("accessibilité", "accessibility"), labels["system"], c["system_intro"])
    page += '<div class="cats-system-points">' + ''.join(f'<article><h3>{e(s["title"])}</h3><p>{e(s["text"])}</p></article>' for s in c["system_points"]) + '</div>'
    page += '<div class="cats-comparison">'
    page += evidence("muesli-documentation", tr("Un cadre documenté", "A documented framework"), tr("Vue d’ensemble de la documentation Muesli : spécification, rédaction et accessibilité.", "Overview of Muesli documentation: specification, writing and accessibility."))
    page += evidence("muesli-detail", tr("Un seul bouton principal par page", "One primary button per page"), tr("Muesli · Primary button. Extrait agrandi des cas d’usage, conservé sans modification.", "Muesli · Primary button. Enlarged usage guidelines, preserved without modification.")) + '</div></section>'

    page += '<section class="cats-section cats-wrap" id="impact">'
    page += section_head("07", labels["impact"], tr("Des contributions à trois niveaux.", "Contributions at three levels."), c["impact_intro"])
    page += '<div class="cats-impact">' + ''.join(f'<article><h3>{e(s["title"])}</h3><p>{e(s["text"])}</p></article>' for s in c["impacts"]) + '</div>'
    page += f'<blockquote class="cats-closing"><p>{e(c["closing"])}</p></blockquote>'
    page += f'<p class="cats-note">{e(tr("Visuels de conception et extraits de recherche, anonymisés. Les schémas éditoriaux sont signalés comme tels. Les écrans présentés ne constituent pas un état des fonctionnalités actuellement en production.", "Anonymised design visuals and research excerpts. Editorial diagrams are labelled. Screens shown do not represent the current production feature set."))}</p>'
    page += f'<div class="cats-footer-nav"><a href="{home_href}#projets">← {e(labels["back"])}</a><a href="mma.html">{e(labels["next"])} →</a></div></section></main>'
    page += f'<script src="{rel}assets/js/cats.js?v=20261029" defer></script>'
    page += contact(landing, rel)
    return page

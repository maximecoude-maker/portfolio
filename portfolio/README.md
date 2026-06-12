# Portfolio Maxime COUDE — Site statique FR/EN

Reproduction en code du prototype Figma « Portfolio ». 14 pages : landing + 6 études de cas, en français et en anglais.

## Structure

```
index.html                 ← Landing FR
projets/*.html             ← 6 études de cas FR (mma, sincro-saas, sincro-mobile, afnor, ratp, hello-promo)
en/index.html              ← Landing EN
en/projects/*.html         ← 6 études de cas EN
assets/css/style.css       ← Design system (Montserrat/Gilroy, #4975E9)
assets/js/main.js          ← Placeholders d'images + animations au scroll
assets/img/                ← À remplir avec les exports Figma (voir IMAGES.md)
build.py + data_fr.py + data_en.py  ← Générateur : modifie les textes ici puis `python3 build.py`
```

## Déployer sur Vercel

1. Crée un repo GitHub (ex. `portfolio`) et pousse tout le dossier.
2. Sur vercel.com → Add New Project → importe le repo → Framework preset : **Other** → Deploy.
   Aucun build n'est nécessaire, ce sont des fichiers statiques.

## Images

Tant que les images ne sont pas exportées depuis Figma, le site affiche des
placeholders hachurés avec le nom du fichier attendu — le site reste donc
parfaitement navigable. Voir **IMAGES.md** pour la liste complète des exports
(clic droit sur le calque dans Figma → Export → PNG 2x → renommer).

## Police Gilroy

Les titres utilisent Gilroy-Bold dans Figma. Cette police n'étant pas sur
Google Fonts, le site retombe automatiquement sur Montserrat ExtraBold (très
proche). Si tu possèdes les fichiers Gilroy (.woff2), dépose-les dans
`assets/fonts/` et ajoute dans style.css :

```css
@font-face {
  font-family: 'Gilroy';
  src: url('../fonts/Gilroy-Bold.woff2') format('woff2');
  font-weight: 800;
}
```

## Modifier les textes

Édite `data_fr.py` / `data_en.py` puis relance `python3 build.py` — toutes les
pages sont régénérées. (Tu peux aussi éditer les .html directement, mais le
générateur évite de répéter 14 fois la même correction.)

## À compléter (repéré dans le Figma)

- Carte « Feedbacks » de la landing : les libellés exacts des chiffres
  (+20 / +250 / 10 M) n'étaient pas lisibles dans la maquette — vérifie-les
  dans `data_fr.py` → `big_stats`.
- La page « CA » (Crédit Agricole) du Figma contient encore le contenu MMA
  (brouillon) et n'est pas reliée à la landing : elle n'a pas été générée.
  Dis-moi quand le contenu sera prêt et on l'ajoutera en 2 minutes.
- Les liens sociaux du footer (LinkedIn, Slack, WhatsApp) pointent vers des
  URL génériques — remplace-les dans `build.py` (bloc SOCIALS).

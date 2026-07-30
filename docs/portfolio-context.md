# Contexte portfolio

## Objectif

Construire un portfolio clair, premium et directement exploitable commercialement pour Maxime Coude, Senior Product Designer UX/UI freelance.

Objectif UX principal : permettre a un prospect de comprendre rapidement le profil, les domaines d'expertise, les preuves projet et les moyens de contact.

## Stack et architecture

- Site statique HTML/CSS/JS.
- Generation via Python : `build.py`.
- Contenus sources : `data_fr.py` et `data_en.py`.
- Pages generees :
  - `index.html`
  - `projets/*.html`
  - `en/index.html`
  - `en/projects/*.html`
- Styles centralises : `assets/css/style.css`.
- JS commun : `assets/js/main.js`.
- Images : `assets/img/`.

## Conventions de code

- Python en snake_case.
- Garder les fonctions petites et explicites.
- Ne pas multiplier les abstractions.
- Les HTML sont des artefacts generes : modifier prioritairement le generateur ou les fichiers data.
- Conserver les textes FR/EN synchronises.

## Direction UX/UI

- Portfolio visuel, editorial, mais lisible.
- Priorite aux cas projets, aux preuves concretes et a la clarte de navigation.
- Cartes projets grand format sur la landing, inspirees du Figma.
- Landing complete : presentation, valeur, projets, clients, contact.
- Ton : professionnel, direct, humain.

## Responsive

- Approche mobile-first.
- Les cartes projets doivent rester lisibles et bien espacees en mobile.
- Verifier les ajustements desktop/mobile dans `assets/css/style.css` avant toute reprise visuelle.
- Toujours verifier :
  - navigation mobile ;
  - lisibilite des titres longs ;
  - absence de chevauchement texte/image ;
  - boutons et liens accessibles ;
  - rendu FR et EN.

## Decisions prises

- Le repo statique versionne est la source de verite.
- La piste React/Vite locale `mon-portfolio` n'est pas la source active.
- Les contenus projet vivent dans `data_fr.py` et `data_en.py`.
- L'etat GitHub actuel genere 14 pages : landing + 6 cas en FR, landing + 6 cas en EN.
- Toute creation d'une page Projets separee doit etre decidee puis implementee proprement depuis l'etat GitHub actuel.

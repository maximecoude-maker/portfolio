# Portfolio Maxime Coude - Memoire projet

Source de verite : ce repository GitHub, pas le dossier local `mon-portfolio`.

## Contexte

Portfolio freelance de Maxime Coude, Senior Product Designer UX/UI. Site statique bilingue FR/EN genere depuis `build.py`, `data_fr.py` et `data_en.py`.

Le site presente une landing avec cartes projets, et six etudes de cas :

- MMA
- Sincro SaaS
- Sincro Mobile
- Afnor
- RATP
- Hello Promo

## Regles de reprise

- Lire ce fichier puis les fichiers utiles dans `/docs` avant de modifier.
- Modifier les contenus dans `data_fr.py` et `data_en.py`, puis regenerer avec `python3 build.py`.
- Eviter d'editer les HTML generes directement sauf correction ponctuelle assumee.
- Conserver la coherence FR/EN.
- Verifier desktop et mobile avant de livrer une modification visuelle.
- Ne pas ajouter de dependance sans besoin clair.
- Ne pas committer de fichiers generes systeme : `__pycache__`, `.DS_Store`.

## Design

Direction actuelle : portfolio statique proche Figma, typographie Montserrat avec fallback Gilroy, accent principal `#4975E9`, cartes projets sur mesure, grands visuels, approche responsive mobile-first.

Details : voir `docs/portfolio-context.md` et `docs/assets.md`.

## Deploiement

Hebergement vise : Vercel via GitHub. Domaine achete chez Hostinger, activation/DNS a confirmer.

Details : voir `docs/deployment.md`.

## Suivi

Taches terminees, en cours et prochaines actions : voir `docs/tasks.md`.

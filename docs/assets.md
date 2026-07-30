# Assets et conventions

## Dossier

Tous les visuels publics vivent dans `assets/img/`.

Sous-dossiers actuels :

- `assets/img/icons/` : icones du toolkit.
- `assets/img/people/` : photos/avatars de remerciements.

## Nommage

Format recommande :

- Projet : `slug-type.png`
- Logo : `logo-marque.png` ou `logo-marque.svg`
- Device/card specifique : `slug-device.png`, `slug-card.png`, `slug-laptop.png`
- Planning : `slug-planning.png`
- Personnes : `prenom-nom.png`

Slugs projet :

- `mma`
- `sincro-saas`
- `sincro-mobile`
- `afnor`
- `ratp`
- `hello-promo`

## Regles

- Preferer PNG 2x pour les exports Figma complexes.
- Preferer SVG pour les logos simples quand disponible.
- Garder les noms stables : ils sont references dans `build.py`, `data_fr.py` et `data_en.py`.
- Ne pas committer `.DS_Store`.
- Documenter tout nouvel asset important dans `IMAGES.md` ou ce fichier.
- Pour les photos de remerciements, utiliser le slug genere depuis le nom :
  minuscules, sans accents, espaces remplaces par des tirets.
  Exemple : `Rémi Joyaux` -> `remi-joyaux.png`.

## Points a verifier

- `IMAGES.md` est partiellement obsolete : plusieurs assets listes existent deja, d'autres nouveaux assets ne sont pas documentes.
- `farid-sayah.png` n'est pas present a date ; le site affiche donc ses initiales automatiquement.

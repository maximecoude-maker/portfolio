# CATS — page web du portfolio

## Résultat

Page intégrée au portfolio statique existant, en français et en anglais :

- `projets/cats.html`
- `en/projects/cats.html`
- Carte CATS en première position sur les deux pages d’accueil.
- Navigation projet suivant et sitemap mis à jour.

Le récit met en avant quatre décisions détaillées, puis un cinquième arbitrage dans le sprint : architecture de gestion multicartes ; exceptions et droits ; sécurité et compréhension ePIN ; confiance Card On File ; chemin jusqu’au premier paiement.

La mission est datée du 2 novembre 2023 au 30 octobre 2026 selon les précisions de Maxime. Le PUC est présenté comme un périmètre parallèle, sans inventer d’écran conseiller.

## Fichiers créés et modifiés

Contenu et génération :

- `data_fr.py` / `data_en.py` : nouveaux dictionnaires `CATS_FR` / `CATS_EN`, contenus existants conservés.
- `cats_page.py` : composition dédiée, intégrée au shell commun ; lecture des dimensions des images avec la bibliothèque standard Python.
- `build.py` : ajout de CATS à la génération FR/EN, aux accueils, aux liens et au sitemap.
- `assets/css/cats.css` / `assets/js/cats.js` : styles de la page, sommaire, focus et fermeture clavier du menu.
- `assets/css/style.css` : ajustement limité à la carte projet CATS.
- HTML FR/EN, accueils et `sitemap.xml` : régénérés par `python3 -B build.py`.

Visuels :

- `assets/img/cats/` : 16 exports WebP, dont une composition avant/après également disponible séparément ; 15 visuels authentiques intégrés dans la page.
- `assets/img/cats-system-fr.svg` / `cats-system-en.svg` : schéma éditorial des trois canaux, explicitement présenté comme tel.
- `docs/cats-assets.json` : source, recadrage, dimensions, empreinte du fichier original et masquages de chaque export.

## Choix visuels et éditoriaux

- Typographies Gilroy / Montserrat et navigation du portfolio conservées.
- Blanc, vert profond et fond menthe ; chiffres en noir.
- Mise en page desktop éditoriale, avec écran mobile authentique dans le hero.
- Comparaison NPC 2023 / 2026, puis trois annotations expliquant le changement de structure.
- ePIN présenté comme un parcours NPC web : aucun faux mockup mobile.
- Notes COF mises en regard, avec la vraie restitution en support.
- Sprint : organisation des ateliers, point d’entrée itéré après les tests, exploration du widget et enseignements du panel.
- Documentation Muesli et extrait agrandi de la règle du Primary button.
- Sommaire sticky, liens d’agrandissement, adaptation mobile, focus visible et respect de la réduction des animations.

## Sources et chiffres

- Les 9 → 13 millions situent uniquement l’échelle de Ma Banque. Aucun lien causal avec la contribution de Maxime.
- Les notes sur 7 sont des notes d’items, pas des scores UMUX-Lite normalisés. Les vagues ne sont pas comparées comme une progression.
- Les notes COF 4,7 / 6,5 et ePIN 6,5 / 6,7 ont été retrouvées dans les captures des restitutions.
- Les résultats 3/4 et 4/4 du sprint restent limités au panel de quatre participants et au prototype.
- Le comparatif 29 % / 96 % n’est pas repris : populations et dénominateurs insuffisamment documentés.
- Aucun verbatim, KPI de conversion ou gain business créé.

## Vérifications et limites

- Génération des 16 pages réussie sans nouvelle dépendance.
- Vérification des ancres, liens locaux, images, dimensions et unicité du titre principal sur les deux nouvelles pages.
- Inspection navigateur desktop et mobile à 390 et 320 px ; menu mobile et navigation de section vérifiés.
- Images originales préservées, vérifiées par empreintes SHA-256. Les masquages concernent les noms, comptes et identifiants ; pas les résultats de recherche ni les valeurs métier.
- Les périodes 2023 / 2026 suivent les dossiers source. Elles ne prouvent pas une date de livraison en production.
- Certains extraits ePIN / carte virtuelle proviennent de planches à faible résolution. Ils sont conservés à une taille limitée, sans recréer les interfaces.
- Le travail d’accessibilité décrit dans le récit ne constitue pas une déclaration de conformité du produit.

## Avant publication

1. Préciser la source et les périodes exactes des volumes d’audience Ma Banque.
2. Distinguer les parcours livrés, les prototypes testés et les recommandations encore ouvertes.
3. Revoir les copies anonymisées avec Maxime dans le contexte de la page finale.
4. Si disponibles, remplacer les petits extraits ePIN / carte virtuelle par des exports Figma HD et ajouter un vrai exemple PUC.
5. Vérifier les données d’exemple de la maquette mobile : certaines valeurs de plafonds / dépensé / restant paraissent incohérentes dans l’original. Elles n’ont pas été corrigées ni présentées comme des résultats.

Version livrée localement. Aucun push ni déploiement en production réalisé dans ce travail.

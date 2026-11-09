# Portfolio Maxime Coude - Memoire projet

Source de verite : ce repository GitHub, pas le dossier local `mon-portfolio`.

## Contexte

Portfolio freelance de Maxime Coude, Senior Product Designer UX/UI. Site statique bilingue FR/EN genere depuis `build.py`, `data_fr.py` et `data_en.py`.

Le site presente une landing avec cartes projets, et sept etudes de cas :

- CATS
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

## CATS — connaissances et compétences durables

Mémoire consolidée le 7 novembre 2026. Sources : brief de Maxime archivé dans `docs/cats-brief-source.md`, précisions explicites du chat, contenus `CATS_FR` / `CATS_EN`, captures originales et `docs/cats-assets.json`. Distinguer toujours une déclaration de contexte, une observation de test, une décision de conception, une recommandation et une livraison en production.

### Mission et posture

- Entreprise : Crédit Agricole Technologies & Services (CATS).
- Mission confirmée par Maxime : **2 novembre 2023 au 30 octobre 2026**, soit près de trois ans.
- Rôle : **Senior Product Designer UX/UI**, principalement sur la **Monétique et les produits cartes bancaires**, sur application, web et portail collaborateur.
- Valeur à démontrer : cadrer et simplifier un système bancaire complexe, réglementé et multicanal ; relier intentions, droits, états, règles métier et interfaces.
- Compétences : cadrage produit, architecture d’expérience, continuous discovery, recherche et restitution, arbitrage, collaboration transverse et conception détaillée.
- Collaboration mentionnée : PO, BA, métiers Monétique, équipes NPC / Ma Banque / PUC, développeurs, Chapter Design, Design System Muesli et accessibilité. Ne pas inventer de management, responsabilité de direction ou résultats personnels exclusifs.
- Exécution directe : architecture de l’information, user flows, wireframes, UI, prototypes Figma, protocoles et animation de tests, documentation et accompagnement du delivery.

### Périmètres et continuité

- **NPC (web client), point de départ** : liste, sélection et détail des cartes ; verrouillage temporaire ; plafonds ; informations carte ; options et paramètres ; opposition ; assurances, garanties et services.
- **Ma Banque (application), extension progressive** : Univers Carte mobile, ePIN, cartes virtuelles, mineurs, opposition, renouvellement e-commerce / Card On File, Apple Pay / In-App Provisioning, Paiement Mobile / CA Pay et Click to Pay.
- **PUC, portail collaborateur conseiller, en parallèle** : pendant conseiller de plusieurs services en autonomie. Penser le relais quand le client demande de l’aide, avec des mots, statuts et conséquences cohérents.
- Ne pas dessiner une migration linéaire NPC → Ma Banque → PUC : NPC d’abord, extension mobile, PUC parallèle.
- Cas à intégrer aux flows : particulier, compte joint, mineur / représentant légal, plusieurs titulaires, multi-comptes, multicartes, droits et éligibilités différents ; carte active, verrouillée, expirée, opposée ou en renouvellement ; support physique ou virtuel.
- Moments de vie : perte / vol, départ à l’étranger, augmentation d’un plafond, paiement en ligne, consultation du PIN, expiration, attente de remplacement, ajout au Wallet.
- Contraintes : authentification forte, sécurité, consentement, RGPD, réglementation, éligibilité, règles métier, legacy, technique, accessibilité et Design System. Ne pas transformer ces contraintes en déclarations de conformité non démontrées.

### Décision personnellement précisée par Maxime

La structure initiale de l’Univers Carte avait atteint ses limites de scalabilité. La lecture très verticale repoussait des contenus sous la ligne de flottaison. Maxime a travaillé au redesign complet vers une **vision de gestion**, construite pour les **profils multicartes**.

Architecture retenue dans le récit : **liste des cartes → carte sélectionnée → statut et actions essentielles → paramètres et services secondaires**. Les actions essentielles doivent rester identifiables, sans allonger indéfiniment la page à chaque nouveau service.

Autres arbitrages documentés :

1. Traiter droits, états et exceptions dans les parcours principaux ; expliquer pourquoi une action dépend du parent ou d’un autre interlocuteur.
2. Rendre l’authentification et la restitution du PIN compréhensibles ; distinguer code SMS et code carte.
3. Concevoir la confiance et le contrôle dans Card On File, au-delà de la seule facilité d’utilisation.
4. Rapprocher l’accès au Paiement Mobile du premier paiement, puis tester l’enrôlement et les premiers usages.

Principes : **clarté, continuité, réassurance, évolutivité**. La complexité doit être absorbée par le système ; l’utilisateur doit disposer des informations nécessaires pour comprendre et agir.

### Recherche continue et données

- Le brief situe Ma Banque à **environ 9 → 13 millions d’utilisateurs actifs mensuels** pendant la mission. Il s’agit d’un **indicateur d’échelle du produit**, jamais d’un impact attribuable à Maxime. Source et dates exactes de mesure à préciser.
- Le brief mentionne plusieurs millions de consultations de l’Univers Carte : pas de volume exact ni de période validés.
- Des centaines d’utilisateurs ont été interrogés à travers différentes campagnes sur le périmètre. Ne pas les attribuer tous à des entretiens personnellement menés par Maxime ni réduire toute la recherche aux cinq vagues ci-dessous. Répartition des contributions et effectifs exacts à documenter.
- Les notes sont des **items bruts sur 7**, pas des scores UMUX-Lite normalisés. Panels et sujets différents : ne pas en déduire une progression entre vagues ni tracer une courbe d’amélioration.
- Les valeurs ci-dessous proviennent du brief ; les notes COF 4,7 / 6,5 et ePIN 6,5 / 6,7 ont aussi été retrouvées dans les restitutions sources. Ne pas qualifier toutes les autres valeurs de vérifiées visuellement.

| Vague | Période | Périmètre et enseignements | Notes fournies |
| --- | --- | --- | --- |
| TU1 | Novembre 2023 | Gestion cartes, verrouillage, plafonds, options, garanties. Accès simple, Quick Link utilisé ; statut expiré ambigu ; personnalisation des plafonds attendue ; « 7 jours glissants » mal compris ; assurances trop génériques. | Environ 6,7/7 sur facilité et réponse au besoin. |
| TU2 | Décembre 2023 | Comparaison V1/V2, multicartes, actions rapides, opposition, informations, paramètres. Navigation simple et actions repérées ; SOS carte et visibilité des options à clarifier. | Pas de note chiffrée fournie dans le brief. |
| TU3 | Novembre–décembre 2024 | CVE de dépannage, Card On File, Univers Carte. Liste & Détail préféré au carrousel ; acceptabilité du COF plus fragile que sa facilité. | CVE : besoin 6,2, facilité 6,4 ; COF : besoin 4,7, facilité 6,5 ; Univers Carte : besoin 5,9, facilité 6,4 (sur 7). |
| TU4 | Avril 2025 | Renouvellement e-commerce, Univers Carte, In-App Provisioning Apple Pay. Protocole sur compréhension, fluidité, rédaction, UMUX-Lite et NPS. | Aucun résultat NPS ou score de cette vague fourni : ne pas en créer. |
| TU5 | Janvier 2026 | Univers Carte, ePIN, CVP, mineurs, opposition en autonomie. ePIN bien reçu ; usage magasin / Wallet et longueur de l’opposition à travailler. | Univers Carte : besoin 5,8, facilité 6,3, compréhension 6,5 ; ePIN : besoin 6,5, facilité 6,5, compréhension 6,7 ; CVP : besoin 5,7, facilité 5,6 ; opposition : besoin 5,2, facilité 5,8 (sur 7). |

Règles de restitution : observation → impact utilisateur → recommandation, sans mélange. Ratios strictement fondés sur les verbatims et leur effectif ; pas de ratio inventé à partir d’une synthèse. Maximum quatre verbatims explicites par point, pas de réutilisation d’une même citation entre plusieurs insights. Aucun verbatim n’a été inventé pour le portfolio.

### Apprentissages par sujet

- **Carte expirée** : la combinaison rouge / pictogramme pouvait évoquer opposition, vol ou alerte. Travailler statut, wording et hiérarchie ; ne pas affirmer un effet mesuré d’une correction sans preuve.
- **Plafonds** : « 7 jours glissants » pouvait être compris comme les sept prochains jours. Une explication ou un affichage date à date est une piste, pas une fonctionnalité livrée confirmée.
- **Actions secondaires** : Paramètres est un repère naturel ressorti des tests ; les actions rapides sont globalement repérées.
- **ePIN** : consulter le PIN en sécurité, visuellement ou en audio ; « Voir le code » préféré ; Securipass rassurant ; confusion possible SMS / PIN ; confidentialité de l’audio en espace public. Le « 10 » visible dans l’export est un compte à rebours ; le PIN était déjà flouté à la source. Les captures retenues sont des parcours **NPC web**, même si le périmètre ePIN plus large couvre aussi Ma Banque.
- **Accessibilité ePIN** : restitution audio, lecteur d’écran, clavier et confidentialité à considérer avec les contraintes techniques Thales mentionnées dans le brief. Les références RGAA 4.10 / 4.11 / 4.12 sont des références citées dans le brief, dont l’applicabilité précise reste à vérifier avant publication. Ne pas déclarer la conformité à partir du seul travail de conception ; distinguer UX et conformité, considérer VoiceOver / TalkBack et navigation clavier.
- **CVE** : carte virtuelle temporaire / de dépannage, pour continuer à payer après opposition en attendant une nouvelle carte. **CVP** : carte virtuelle permanente. Ne pas les confondre. Usage en ligne plus évident que l’usage en magasin ; expliquer le Wallet, l’ajout et la différence online / magasin, sans allonger la pédagogie inutilement.
- **Mineurs** : restrictions globalement comprises et acceptées ; besoin d’explication, statut visible et possibilités de demande / notification au parent. Exemple du brief : « Carte verrouillée — seul votre parent peut la déverrouiller. » Les mécanismes de demande et notification restent des pistes si leur livraison n’est pas confirmée.
- **Opposition en autonomie** : parcours compris et rassurant, mais parfois trop long en situation de perte / vol. Pistes : accès SOS, étapes raccourcies, remplacement / délai / frais explicites, modification d’adresse dans le flow. Pas d’effet en production démontré.
- **Card On File / renouvellement e-commerce** : actualisation automatique des données de carte auprès de certains commerçants au renouvellement. Facilité ne signifie pas adhésion : bénéficiaires, circulation des données, consentement révocable et contrôle insuffisamment compris. L’écart 6,5/7 facilité vs 4,7/7 besoin est une preuve centrale du récit.
- **Apple Pay / In-App Provisioning** : point d’entrée, sélection de carte, authentification, transition Ma Banque ↔ Apple, confirmation, second appareil tel qu’Apple Watch ; concevoir aussi les retours et changements de contexte.
- **Click to Pay** : contribution récente à l’enrôlement, consentement, sélection de carte, coordonnées, adresse, activation et gestion / suppression. Questions : consentement replié ou développé, carte verrouillée, wording, fermeture du tunnel. Protocole sur compréhension, navigation, connaissance et confiance ; pas de résultats chiffrés fournis. Sujet secondaire démontrant l’accueil de nouveaux services.

### Sprint Paiement Mobile / CA Pay

- Dates : **19, 20 et 21 mai 2026**. Explorer la reprise de Paiement Mobile CA, application auparavant distincte, dans Ma Banque.
- Contexte du brief : expérience fragmentée, activation / configuration complexes, réinstallations, adoption limitée, préférence pour Apple Pay et coût iOS. Ne pas inventer de coût ni de mesure d’adoption.
- Jour 1 : Lean Canvas, benchmark, données, Experience Map, How Might We ; cadrage commun.
- Jour 2 : 5 Why’s, Big Idea, Idea Wall, user flow et wireframes ; idéation et convergence.
- Jour 3 : prototype et tests utilisateurs.
- **3/4** trouvent l’accès plus simple grâce à l’intégration à Ma Banque ; **4/4** trouvent l’enrôlement simple, fluide et rassurant. Ces ratios décrivent un panel de quatre sur un prototype, pas une adoption ni un effet de déploiement.
- Points ouverts : sélection des cartes, « Activer par défaut », jargon NFC, tutoriel du premier usage et compréhension du cashback.
- Deux moments à relier : enrôlement et paiement. Priorité de conception : réduire le chemin jusqu’au premier paiement et accompagner son usage ; pas de gain mesuré à affirmer.
- Le comparatif **29 % Paiement Mobile / 96 % Apple Pay** du brief a été écarté de la page : population, période, dénominateur et comparabilité à documenter avant tout usage.
- Recommandation produit mémorisée de Maxime : ouvrir CA Pay aux cartes d’autres banques pour les clients multibancarisés. C’est une recommandation, pas une décision livrée confirmée.

### Design System chez CATS — Muesli

Dans sa mission chez CATS, Maxime concevait les parcours cartes dans le cadre de Muesli : réutilisation des composants, cohérence des actions et des états, UX Writing, accessibilité et échanges avec l’équipe Design System.

Note dédiée dans Obsidian : [[memory/projects/design-system-muesli|Design System Muesli]], avec deux preuves intégrées au vault, les règles des composants et leur statut de vérification.

- Chercher d’abord la solution dans le Design System Muesli, puis questionner ou faire évoluer le pattern si le contexte l’exige ; ne pas créer un composant par défaut.
- Patterns mentionnés : Primary / Secondary button, Link, Chips, Bottom sheet, Button keyboard, navigation, formulaires, tableaux, visualisation de données et tunnels.
- Documentation : aperçu, spécifications, tokens, états, guidelines UX/UI, UX Writing, animation et accessibilité.
- Règle Primary confirmée par un extrait : **un seul bouton principal par page**. Autres consignes du brief : libellé concis, verbe à l’infinitif, environ 20 caractères maximum, pas de point final, placement généralement en bas.
- Secondary : action secondaire, normalement pas utilisé seul, cohérence de largeur avec Primary ; espacement de 32 px cité dans le brief, à vérifier dans la version de la documentation concernée avant application systématique.
- Prendre en compte contrastes, rédaction, zoom 200 %, restitution audio et lecteurs d’écran ; RGAA / RAAM selon le périmètre applicable. Ne pas présenter ces travaux comme un audit de conformité.

### Page Crédit Agricole — refonte du 7 novembre 2026

- La page `projets/cats.html` (et `en/projects/cats.html`) n'est plus une page sur mesure : c'est désormais la **7e entrée de `PROJECTS_FR` / `PROJECTS_EN`**, placée en tête, construite par le gabarit générique `build_case` comme les six autres études de cas. L'URL et le slug `cats` sont inchangés.
- Source de conception : maquette Figma « Portfolio Maxime COUDE », frame **« CA » (node 1127-10249)**, lue via le serveur **Dev Mode MCP local** (port 3845). Ce frame est une duplication du frame « MMA » : son corps contenait encore le texte MMA, remplacé par le contenu réel CATS. Tokens relevés : H2 Gilroy-ExtraBold 64/1.2, H3 Gilroy-Black 40/1.2, Body L Montserrat Medium 24/1.5, KPI Gilroy-ExtraBold 120/100.
- Couleurs reprises du frame : teal `#004652` (accent et titre, à la place du violet MMA `#2b097c` resté dans la maquette), menthe `#d8ead7` (panneau derrière les écrans), fond blanc.
- Les 8 mockups iPhone de la section « User interface » étaient **vides** dans Figma. Ils sont remplacés par les trois vrais écrans Ma Banque présents dans le hero du frame, récupérés en pleine résolution depuis le serveur d'assets Figma : `assets/img/ca/manage-card`, `card-details`, `card-services` (PNG + WebP).
- **Anonymisation** : nom du titulaire, numéro de carte, date de fin de validité et cryptogramme masqués par remplissage échantillonné sur le dégradé de la carte. Provenance, empreintes et zones masquées dans `docs/ca-assets.json`. Ne jamais republier les exports bruts.
- Nouveau rendu générique dans `build.py` : `devices_html()` et la clé `hero_devices` / un dict `{"devices": [...]}` dans `research` ou `solution`. CSS `.device-row` / `.device` en fin de `assets/css/style.css`. **Device frame réservé aux vraies captures d'écrans mobiles** ; les captures NPC web de `assets/img/cats/` restent en figure simple.
- `cats_page.py`, `cats.css` et `cats.js` sont déplacés dans `archive/` : plus aucune page ne les référence depuis la refonte. `CATS_FR` / `CATS_EN` restent dans les fichiers de données, marqués ARCHIVE et plus importés par `build.py`. Les chemins `assets/css/cats.css` / `assets/js/cats.js` cités plus bas décrivent l'état historique du 29 octobre.
- Section « Les impacts » : les cinq placeholders « x % » de la maquette sont remplacés par des **items bruts sur 7 issus des protocoles de tests**, avec un chapeau qui précise qu'il ne s'agit ni de scores normalisés ni d'indicateurs business, et que les vagues ne décrivent pas une progression. Aucun KPI business n'a été inventé.
- Section « Remerciements » : aucun nom de coéquipier CATS n'étant documenté, les profils portent des **libellés de rôles** (Product Owners, Business Analysts, Métiers Monétique, NPC Web, Ma Banque, Portail PUC, Développeurs, Chapter Design, Design System Muesli, Référents accessibilité). Remplacer par de vrais noms dès que Maxime les fournit.
- Vérifications effectuées le 7 novembre 2026 : build 16 pages, aucune image manquante, aucun débordement horizontal, un seul H1, desktop et mobile 375 px, FR et EN. **Aucun commit ni déploiement effectué.**

### Projet CATS masque — 9 novembre 2026

- Sur demande de Maxime, le projet `cats` porte `"hidden": True` dans `PROJECTS_FR` / `PROJECTS_EN`.
- Effet : carte retiree des deux accueils, projet saute dans la navigation de bas de page (`next_visible()` dans `build.py`), URL absente du `sitemap.xml`, et page servie avec `<meta name="robots" content="noindex, nofollow">`.
- La page reste generee et accessible par son URL directe `projets/cats.html` / `en/projects/cats.html` : le lien peut encore etre partage a la main. Le build produit toujours 16 pages.
- Les visuels `assets/img/ca/` et `assets/img/cats/` restent publies et accessibles par leur URL. Pour les retirer aussi, il faut une depublication explicite.
- Repasser `hidden` a `False` dans les deux fichiers de donnees suffit a republier le projet.

### Portfolio : récit, implémentation et état connu

- Angle : **« Une expérience Carte cohérente, du client au conseiller. »** Le lecteur doit comprendre les arbitrages et la manière de penser de Maxime, pas seulement parcourir une succession de livrables.
- Récit : problème → hypothèse → décision → apprentissage. Impact utilisateur, produit et collectif décrit qualitativement ; aucun KPI business inventé.
- Page web FR/EN, environ dix minutes de lecture. Routes `projets/cats.html` et `en/projects/cats.html`, carte CATS en tête des accueils, navigation des projets et sitemap mis à jour.
- Source du site : ce dépôt statique, pas l’ancien prototype React ni une maquette CA.pdf reprenant le texte MMA.
- Contenu : `data_fr.py` → `CATS_FR`, `data_en.py` → `CATS_EN`. Composition : `cats_page.py`. Génération : `python3 -B build.py` → 16 pages au total.
- Styles : `assets/css/cats.css` et ajout limité à la carte CATS dans `assets/css/style.css`. Navigation de section et Échap : `assets/js/cats.js`. Shell partagé via `build.py`.
- Direction : Gilroy pour les titres / Montserrat pour les textes, navigation existante, blanc, vert profond `#173F35`, menthe `#EAF3EF`, chiffres en noir ; grand texte, espace, compositions explicatives. Pas de mini-site isolé ni de dépendance ajoutée.
- Hero : vraie maquette Ma Banque dans un cadre mobile, extrait visible avec accès à l’image complète. Sommaire sticky ; comparatif NPC ; preuves ePIN ; recherche ; sprint ; documentation Muesli et règle agrandie ; contributions.
- Vérifications réalisées pendant la session de création : génération, ancres et liens, images et dimensions, un H1, FR/EN, desktop 1280 px, mobile 390 / 320 px, menu et Échap, réduction des animations ; aucun débordement horizontal ni image chargée cassée observés au dernier contrôle.
- Dernière livraison documentée : **29 octobre 2026, version locale**. Aucun push / déploiement n’a été effectué pendant cette session. Un éventuel changement de production ultérieur n’a pas été vérifié.
- L’URL locale `http://127.0.0.1:8765/projets/cats.html` exige un serveur actif : ne pas la considérer comme une URL de production ni présumer que le serveur tourne encore.

### Assets : provenance, sens et réutilisation

Dossier réellement fourni : `/Users/macbookpromxm/Documents/Travail/[05] - Radness Studio - Freelance/CATS/`. L’arborescence `/public/cats/` initialement citée n’existait pas dans l’environnement ; ne pas y chercher les originaux par défaut.

Inventaire de la session : 160 PNG, un PDF et un HTML. Le PDF `App MB Carte/CA.pdf` était une ancienne maquette de portfolio réutilisant du texte MMA, pas une preuve produit CATS.

Exports dans `assets/img/cats/` : **16 WebP, 615 806 octets**, dont une composition disponible séparément ; **15 visuels réels intégrés**. Sources, hashes SHA-256, dimensions, recadrages, masques et datation sont dans `docs/cats-assets.json`. Les originaux ont été conservés et vérifiés par empreinte.

| Clés des exports | Signification correcte |
| --- | --- |
| `universe-before`, `universe-after`, `universe-comparison` | NPC web, versions des dossiers 2023 et 2026. Comparaison de conception, pas dates de mise en production démontrées. |
| `universe-detail` | Paramètres NPC, dossier 2026 ; actions secondaires. |
| `universe-mobile` | Maquette Ma Banque, capture du 26 octobre 2026 ; date de conception exacte non établie. |
| `epin-choice`, `epin-visual`, `epin-audio` | Écrans NPC web, extraits du protocole TU5 (janvier 2026 selon le brief). Ne pas les encadrer comme des écrans mobiles. |
| `virtual-cards` | CVP NPC web, protocole TU5 ; ne pas la légender comme CVE ni comme capture mobile. |
| `research-tu3` | Vraie restitution COF avec les items 4,7/7 besoin et 6,5/7 facilité. |
| `sprint-map` | Organisation des ateliers / trois journées ; ce n’est pas la carte d’expérience elle-même. |
| `sprint-enrolment` | Point d’entrée CA Pay retravaillé **après les tests**, pas le parcours complet d’enrôlement initial. |
| `sprint-payment` | Exploration d’un accès depuis le widget Ma Banque, pas une transaction ou preuve d’usage en production. |
| `sprint-research` | Éléments appréciés par le panel de quatre, pas une slide d’irritants. |
| `muesli-documentation` | Vue d’ensemble des spécifications et guidelines du composant **Link** ; capture du 26 octobre 2026, mise à jour visible du 2 décembre 2025. |
| `muesli-detail` | Vrai extrait Primary button : un seul bouton principal par page. |

- Deux SVG `cats-system-fr.svg` / `cats-system-en.svg` expliquent les trois canaux : illustrations éditoriales signalées, pas interfaces produit ni livrables CATS réels.
- Aucun vrai écran PUC n’a été trouvé. Utiliser le schéma de continuité tant qu’un exemple authentique n’est pas fourni.
- Maxime a autorisé la diffusion des écrans et données **avec anonymisation**, en indiquant qu’il préciserait les sources. Masquer noms, comptes, identifiants et codes sensibles, pas les chiffres de recherche ni les valeurs métier. Ne pas remplacer ces données par des chiffres inventés.
- Les petits extraits ePIN / CVP ont une résolution source limitée, environ 330 px. Pas de recréation ou d’agrandissement artificiel de l’interface. Préférer des exports Figma HD si disponibles.
- Chaque visuel doit expliquer une décision, une évolution ou un apprentissage. Avant/après, comparaison de canaux et annotations limitées sont préférables à une galerie décorative. Device frame uniquement pour de vrais écrans mobiles ; browser frame pour web ; préciser les périodes distinctes.
- Certaines valeurs d’exemple de plafonds / dépensé / restant de la maquette mobile paraissent incohérentes dans l’original. Elles ont été conservées, pas corrigées ni utilisées comme KPI.

### Skills Codex et méthodes de travail

Compétences métier et skills d’agent ne sont pas interchangeables. Les compétences Product Design de Maxime sont décrites plus haut ; les fichiers ci-dessous guident la reprise technique.

| Skill / outil | Statut réel et utilité |
| --- | --- |
| `frontend-design` — `/Users/macbookpromxm/.codex/skills/frontend-design/SKILL.md` | Utilisé pour construire la page : direction éditoriale, cohérence avec le portfolio, qualité responsive et visuelle. |
| `memory` — `/Users/macbookpromxm/.codex/skills/memory/SKILL.md` | Utilisé pour cette consolidation : notes durables, sources, incertitudes et distinction entre historique et état actuel. |
| `sites:sites` | Workflow consulté dans sa version 1.1.2 pendant la création. Le site existant a été modifié localement dans son dépôt Vercel ; aucun Site hébergé par le plugin n’a été créé ou publié. Le chemin installé peut changer : retrouver la version disponible si nécessaire. |
| `pdf:pdf` | Consulté par le sous-agent pour examiner `App MB Carte/CA.pdf`, puis écarté : ancienne maquette portfolio reprenant MMA, aucune preuve CATS retenue. |
| Computer use `cua_repl` | Outil utilisé pour observer le portfolio et vérifier le rendu / les interactions navigateur. Ce n’est pas un skill métier ni une preuve de test sur téléphone réel. |
| Python / traitement des captures | Préparation déterministe des recadrages et masques, conversion WebP, manifest de provenance. Générateur final en bibliothèque standard, sans nouvelle dépendance. Aucun faux écran généré par IA. |

Selon une future demande, mobiliser un skill supplémentaire seulement si utile : Figma pour un vrai lien / export Figma ; code-review pour une revue ; accessibilité et animation selon le travail demandé. Réutiliser PDF si un nouveau document l’exige. **Ne pas présenter un skill disponible comme déjà utilisé sans trace, ni installer tout le catalogue.** Lire les prérequis du skill correspondant au moment de l’utiliser.

### Points à compléter avant publication ou nouvelle affirmation

1. Source et périodes exactes des audiences 9 → 13 M et des volumes Univers Carte.
2. Statut livré / testé / recommandé de chaque évolution ; contribution personnelle détaillée sur les autres arbitrages.
3. Effectifs et références précises de chaque vague si des ratios supplémentaires sont ajoutés.
4. Revue des copies anonymisées dans la page finale ; exemple PUC authentique et exports HD ePIN / CVP si disponibles.
5. Applicabilité précise des critères RGAA cités et résultats d’audit éventuels.
6. Contrôle des données d’exemple incohérentes sans altérer les captures d’origine.

Pour reprendre : lire cette section, `docs/cats-delivery.md`, le manifest et les contenus FR/EN ; régénérer depuis les sources, vérifier le rendu et ne pas déployer ou réattribuer des résultats sur la base d’un état historique non revérifié.

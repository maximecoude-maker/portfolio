# Deploiement

## Etat connu

- Repository GitHub : `https://github.com/maximecoude-maker/portfolio.git`
- Branche principale : `main`
- Hebergement cible : Vercel
- Framework Vercel attendu : `Other`
- Build Vercel : aucun build obligatoire, le site est statique.
- Domaine : achete chez Hostinger, activation/DNS a confirmer.

## Deploiement attendu

Le site peut etre servi directement depuis les fichiers statiques versionnes.

Workflow recommande :

1. Modifier les sources : `build.py`, `data_fr.py`, `data_en.py`, CSS ou assets.
2. Regenerer les pages : `python3 build.py`.
3. Verifier localement.
4. Committer.
5. Pousser sur `main`.
6. Laisser Vercel redeployer via l'integration GitHub.

## Configuration Vercel a confirmer

Le repo local ne contient pas encore :

- `.vercel/project.json`
- `vercel.json`

Donc la liaison exacte Vercel/projet/domaine n'est pas verifiable depuis le repo seul.

## Point local a corriger

Le Vercel CLI local ne fonctionne pas actuellement parce que la commande `node` active pointe vers une ancienne version (`v12.12.0`) alors que le CLI installe attend un runtime moderne.

Action recommandee :

- activer Node 20+ avant d'utiliser `vercel`;
- puis verifier `vercel ls`, `vercel domains ls` ou le dashboard Vercel.

## Domaine Hostinger

A documenter des que l'activation est terminee :

- nom de domaine exact ;
- type de configuration DNS choisie ;
- cible Vercel ;
- statut SSL ;
- date de verification.

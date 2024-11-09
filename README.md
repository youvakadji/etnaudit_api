# Déploiement de l'Application Django sur Heroku

Ce document décrit les étapes nécessaires pour déployer cette application Django sur Heroku en utilisant GitHub Actions pour l'intégration et le déploiement continus (CI/CD).

## Prérequis

1. **Heroku** : Créez un compte sur [Heroku](https://heroku.com) si vous n'en avez pas encore.
2. **API Key Heroku** : Récupérez votre clé API Heroku depuis [Account Settings](https://dashboard.heroku.com/account).
3. **GitHub** : Créez un dépôt GitHub pour votre projet si ce n’est pas déjà fait.

## Configuration de Heroku

### 1. Créer une Application Heroku

- Connectez-vous à votre compte Heroku.
- Créez une nouvelle application en cliquant sur **New** > **Create new app**.
- Donnez un nom à l'application (ex. `etnauditapi`) et sélectionnez la région.

### 2. Configurer les Variables d’Environnement sur Heroku

Si votre application Django utilise des variables d'environnement (comme `SECRET_KEY`, `DATABASE_URL`), configurez-les dans **Settings** > **Config Vars** de votre application Heroku.

### 3. Créer un Procfile

Un `Procfile` est nécessaire pour dire à Heroku comment exécuter votre application.

- Créez un fichier `Procfile` à la racine de votre projet.
- Ajoutez la ligne suivante dans le `Procfile` pour spécifier le point d’entrée de l’application :

  ```plaintext
  web: python back_end/manage.py runserver 0.0.0.0:$PORT

## Configuration de GitHub Actions pour CI/CD
GitHub Actions est utilisé ici pour mettre en place un pipeline CI/CD qui automatise les étapes de test et de déploiement sur Heroku.

### 1. Ajouter un Secret Heroku dans GitHub
  1. Allez dans votre dépôt GitHub.
  2. Allez dans Settings > Secrets and variables > Actions > New repository secret.
  3. Ajoutez un secret nommé HEROKU_API_KEY et collez-y votre clé API Heroku.

### 2. Créer le Workflow GitHub Actions
Dans votre dépôt GitHub, créez un fichier .github/workflows/deploy.yml pour configurer le workflow de déploiement.

### Explication du Workflow
1. Build : Clonage du code, configuration de Python, installation des dépendances et collecte des fichiers statiques.
2. Test : Exécution des tests unitaires définis dans audit/tests.
3. Deploy : Déploiement sur Heroku si les tests réussissent.

### Déclenchement Automatique du Déploiement
Le pipeline CI/CD se déclenche automatiquement sur GitHub Actions après chaque push sur la branche main. Le workflow effectue les étapes de test et, si tout passe, déploie automatiquement l’application sur Heroku.

## Conclusion
Avec cette configuration, vous avez un pipeline CI/CD complet pour votre application Django sur Heroku en utilisant GitHub Actions. Cela permet de s’assurer que l’application est testée et déployée automatiquement en production après chaque mise à jour de la branche main.

Pour plus d’informations, consultez :

- Documentation Heroku
- Documentation GitHub Actions
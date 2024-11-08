# ETNAUDIT API

## Description

Ce projet est une API RESTful construite avec **Django** et **Django REST Framework**. Elle permet de gérer des articles, avec des fonctionnalités de récupération des données sous format JSON.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- Pip (le gestionnaire de paquets Python)

## Installation

### Installez les dépendances :

```bash
pip install -r requirements.txt
```

Si le fichier requirements.txt n'existe pas encore, vous pouvez l'ajouter en générant la liste des dépendances installées avec la commande suivante :
```bash
pip freeze > requirements.txt
```

Creer une migration:
```bash
python manage.py makemigrations

ou 

python3 manage.py makemigrations
```

Appliquez les migrations à la base de données :
```bash
python manage.py migrate

ou 

python3 manage.py migrate
```

Créez un super-utilisateur pour accéder à l'interface d'administration (facultatif) :

```bash
python manage.py createsuperuser
```

Lancez le serveur de développement :
```bash
python manage.py runserver

ou 

python3 manage.py runserver

```
L'API sera accessible à l'adresse suivante : http://127.0.0.1:8000/.


## Lancer les tests

Pour lancer les tests il suffit de faire la commande : 

python manage.py test audit/tests/

Pour lancer les tests d'un fichier précis il suffit de faire par exemple :

python manage.py test audit.tests.test_models
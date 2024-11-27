## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement du site Orange County Lettings est automatisé via un pipeline CI/CD configuré sur GitHub Actions. 
Ce pipeline permet de tester, conteneuriser et déployer l’application sur la plateforme Render.

### Récapitulatif du Déploiement

#### Tests et Linting

- Lorsqu’un nouveau commit est poussé sur GitHub (toute branche), le pipeline CI/CD exécute des tests unitaires avec pytest et vérifie la qualité du code avec flake8. 
- La couverture des tests doit être supérieure à 80 % pour passer cette étape.

#### Conteneurisation

Si tous les tests sont réussis et qu'il s'agit de la branche QA ou master, une image Docker de l’application est construite et poussée vers Docker Hub. L’image est étiquetée avec le hash de commit correspondant ({{github.sha}}), garantissant que chaque version est unique.

#### Déploiement sur Render

Une fois l’image Docker disponible sur Docker Hub, le pipeline déclenche le déploiement sur Render, où l’application est mise en production. Seuls les commits sur la branche master déclenchent cette étape.

### Configuration Requise pour le Déploiement

Pour que le déploiement fonctionne correctement, les éléments suivants doivent être configurés :

#### Secrets GitHub

Le projet utilise des secrets pour sécuriser l’accès aux services externes :
    - DEBUG : Mode debug True ou False.
    - SENTRY_DSN : URL de connexion pour le suivi des erreurs via Sentry.
    - ALLOWED_HOSTS : la liste des hebergeur autorisé, séparé par une virgule.
    - DOCKER_USERNAME : Nom d’utilisateur Docker Hub.
    - DOCKER_PASSWORD : Mot de passe Docker Hub.
    - RENDER_API_KEY : Clé API pour déployer sur Render. (voir section suivante)
    - RENDER_SERVICE_ID : le service id du serveur Render. (voir section suivante)

#### Configuration Render

Un service web Docker doit être configuré sur Render pour recevoir l’image Docker et exécuter l’application.

### Étapes pour Déployer

#### Configurer le service sur Render

  Créez un nouveau Web Service sur Render.
  Choisissez Existing Image comme source et configurez le service pour utiliser l’image Docker de votre projet (l'image sera géré par le pipeline une fois configuré).
  Configurer un Disk pour la base de donnée.
  Dans les option du compte allez créer une clé API (qui iras dans la variable RENDER_API_KEY).
  Votre Service ID et trouvable dans l'url du projet render et devrais resembler à quelque chose comme ça srv-csvji4m8ii6s73eu6tk2 (il est aussi possible de le voir dans la section SSH du menu connect).
  
  Ajoutez les variables d’environnement nécessaires (voir la section précédente).
    - ALLOWED_HOSTS : adresse autorisé (la ou les adresses ou le site peut être accessible, séparer par des virgule.).
    - SECRET_KEY : La clé secrète Django.
    - DEBUG : False en production.
    - SENTRY_DSN : Pour le suivi des erreurs via Sentry.
    - PORT : 8000
    - DB_PATH : chemin vers la DB sur le disk.
    
  Assurez-vous que le port est configuré à 8000.

#### Déployer depuis GitHub

  Poussez vos modifications sur la branche master de votre repository GitHub.
  Le pipeline GitHub Actions sera automatiquement déclenché :
      Étape 1 : Les tests et le linting sont exécutés.
      Étape 2 : Si les tests sont réussis, une nouvelle image Docker est construite et poussée sur Docker Hub.
      Étape 3 : Render est informé de l’image mise à jour et déploie automatiquement la nouvelle version de l’application.

#### Vérifier le déploiement

  Une fois le déploiement terminé, rendez-vous sur l’URL de votre service Render.
  Vérifiez que :
      Le site est accessible.
      Les fichiers statiques (CSS, JS) sont correctement chargés.
      Le panel d’administration est fonctionnel.

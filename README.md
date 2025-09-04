# 🏡 California House Price Predictor

Ce projet est une application de Machine Learning qui prédit le prix médian des maisons en Californie à partir du dataset **California Housing** de scikit-learn.

Il comporte deux interfaces principales :
- Une API REST développée avec **FastAPI**
- Une interface web simple développée avec **Streamlit** pour interagir avec le modèle

---

## ⚙️ Création de la structure du projet

La structure du projet a été générée automatiquement via un script setup.sh y compris la création du répertoire du projet california-price-predictor.

**1.** Script d'initialisation (setup.sh)

```bash
#!/bin/bash

# Nom du projet
PROJECT_NAME="price-predictor-california"

# Création des dossiers
mkdir -p $PROJECT_NAME/{app,tests,scripts,.github/workflows}

# Création des fichiers dans app/
touch $PROJECT_NAME/app/__init__.py
touch $PROJECT_NAME/app/api.py
touch $PROJECT_NAME/app/model.py
touch $PROJECT_NAME/app/streamlit_app.py
touch $PROJECT_NAME/app/utils.py


# Tests
touch $PROJECT_NAME/tests/test_model_simple.py
touch $PROJECT_NAME/tests/test_placeholder.py

# Scripts
touch $PROJECT_NAME/scripts/preprocess.py
touch $PROJECT_NAME/scripts/train_model.py

# GitHub Actions (CI/CD)
touch $PROJECT_NAME/.github/workflows/ci.yml

# Fichiers racine
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/.gitignore

echo "Structure du projet $PROJECT_NAME créée avec succès ✅"
```

**2.** Donner les droits d’exécution au script :
```bash
chmod +x setup.sh
```

**3.** Lancer le script :
```bash
./setup.sh
```

Cela crée automatiquement l’arborescence suivante :
```bash

california-price-predictor/
│
├─ app/
|  ├─__init__.py         # Création d'un fichier init
│  ├─ api.py            # API FastAPI
│  ├─ model.py          # Chargement et prédiction du modèle
│  ├─ utils.py          # Fonctions utilitaires (prétraitement)
│  └─ streamlit_app.py  # Interface Streamlit
│
├─ scripts/
│  ├─ preprocess.py 
│  ├─ train_model.py    # Script pour entraîner le modèle
├─ tests/
│  ├─ test_placeholder.py 
│  ├─ train_model_simple.py   
├─ model.joblib         # Modèle entraîné (généré après exécution)
├─ requirements.txt     # Dépendances Python
├─ setup.sh             # Script d’initialisation du projet
├─ .gitignore           # Script permettant d'ingorer certains fichier lors du push dans Github
└─ README.md            # Documentation
```

## 📂 Initialisation du projet

### 1. Création du dépôt GitHub

1. Aller sur GitHub (https://github.com/) et créer un nouveau repository (ex: `california-price-predictor` comme le nom du projet local créé dans VScode).  
2. Copier l’URL HTTPS du dépôt.  

### 2. Connexion du projet local à GitHub

Dans le dossier du projet local :  

```bash
git init
git remote add origin <URL_DU_DEPOT>
git branch -M main
```

Ensuite, pour pousser les fichiers sur GitHub :
```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 📦 Installation

**1.** Créer un environnement virtuel Python 3.10+ :

```bash
python -m venv env-california-price-predictor
```

**2.** Activer l’environnement :

Linux/macOS :
```bash
source env-california-price-predictor/bin/activate
```

Windows :
```bash
.\env-california-price-predictor\Scripts\activate
```

**3.** Installer les dépendances :
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📓 Utiliser Jupyter Notebooks pour l’analyse exploratoire

**1.** Installer Jupyter si ce n’est pas déjà fait :
    
```bash
pip install notebook ipykernel
```

**2.** Ajouter l’environnement virtuel comme kernel Jupyter :

```bash
python -m ipykernel install --user --name=env-california-price-predictor --display-name "Python (california-predictor)"
```

**3.** Créer vos notebooks dans le dossier notebooks/.

**4.** Lorsque vous ouvrez Jupyter (jupyter notebook ou via VSCode), sélectionnez le kernel :

Python (california-predictor)

👉 Cela garantit que vos notebooks utilisent bien les mêmes dépendances que l’application FastAPI et Streamlit.


## 🧠 Entraînement du modèle

Le modèle est basé sur Linear Regression pour prédire le prix médian des maisons.
Avant de lancer la commande pour l'entrainement du modèle entrainé dans le fichier scripts/train_model.py, on peut créer un notebok train_model.ipynb pour tester les différentes étapes.

```bash
python -m scripts.train_model

```
Cela sauvegardera le modèle entraîné dans model.joblib dans la raceine du projet.


## 🚀 Tester l’API FastAPI

**1.** Lancer le serveur FastAPI :
```bash
uvicorn app.api:app --reload
```

**2.** Accéder à l’interface Swagger pour tester :
```bash
http://127.0.0.1:8000/docs
```

**3.** Exemple de requête POST /predict :
Sur la ligne POST, on clique sur la fleche tout à droite, ensuite sur le bouton "Try it out".
Dans le corps de la requête "Request by" on copie les valeurs du dictionnaire suivant

```bash
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 1.0238,
  "AveBedrms": 0.5556,
  "Population": 322.0,
  "AveOccup": 2.5556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```
Ensuite onn clique sur Exécute.
Le résultat devrait être :
```bash
{
  "prediction": 4.13164641129476
}
```

## 🌐 Interface Streamlit

**1.** Lancer Streamlit :
```bash
streamlit run app/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```
Ou 
```bash
streamlit run app/streamlit_app.py
```
Le fichier streamlit_app.py doit faire appel à l'adresse locale de FastAPI "http://127.0.0.1:8000/predict" mais pas celle prévue pour Docker "http://api:8000/predict".

Si un message d'erreur lié à protobuf, il y'a une solution de contournement qui permet d'exporter la variable d'environnement (exécute cette dernière commande d'abord):
**1.** Lancer Streamlit :
```bash
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```

**2.** L’interface web sera accessible ici :
```bash
http://localhost:8501
```

## ⚙️ Dépendances principales
Ci-dessous les dépances principales qui sont validées dans ce projet :

```bash
fastapi==0.115.5
starlette==0.41.0
uvicorn==0.30.6
httpx==0.27.2
pytest==8.4.1
anyio==3.7.1
numpy==1.23.5
pandas==1.5.3
scikit-learn==1.2.2
joblib==1.2.0
python-multipart==0.0.6
flake8==7.3.0
black==23.12.0
protobuf==3.20.3
streamlit==1.24.0
```

## 📌 Notes
```bash
  - Assurez-vous que l’environnement virtuel actif correspond à celui utilisé pour installer les dépendances.
  - Si le modèle model.joblib a été généré avec une autre version de Python, supprimez-le et réentraînez-le avec votre version actuelle.

```

## 🚀 Evolution du projet

**1.** Créer une nouvelle branche

Exemple de création de branche :

```bash
git checkout -b feature/train-test-split
```

**2.** Valider la branche

Si tout est bon, commiter et push la branche vers le dépôt github :

```bash
git add .
git commit -m "Ajout du split train/test avec random_state pour reproductibilité"
git push origin feature/train-test-split

```

Ensuite, sur GitHub, tu pourras créer une Pull Request pour merger cette branche dans main.

  **1.** Créer un Pull Request (PR)

  Va sur ton dépôt GitHub.

  Tu verras un bouton "Compare & pull request" pour ta branche.

  Clique dessus, ajoute un titre et une description. Clique sur le bouton "Create pull request"

  Assigne une ou plusieurs personnes comme reviewers.


  **2.** Relecture et approbation

  Les reviewers peuvent commenter, demander des changements ou approuver le PR.

  Tu peux faire des commits supplémentaires sur la branche si tu corriges quelque chose ; ils se mettront automatiquement dans le PR.


  **3.** Fusionner la branche

  Une fois que la PR est approuvée, tu peux la merger dans la branche principale (main ou master) via GitHub en cliquant sur le bouton "Merge pull request", ensuite sur "Confirm merge".

  Ensuite, tu peux supprimer la branche si elle n’est plus nécessaire :

```bash
git branch -d feature/train-test-split       # locale
git push origin --delete feature/train-test-split  # distante
```

Depuis le projet local :

**1.** Retourner sur la branche principale (main) :

```bash
git checkout main
```
**2.** Récupérer les derniers changements depuis GitHub :

```bash
git pull origin main
```


Test effectués : 

- test_model_simple

- test_placeholder


Tests, lintings et formatage :

1. Lancer les tests :
```bash
pytest tests/ --maxfail=1 --disable-warnings -v
```

2. Vérification le linting et le formatage 

```bash
black --check .
#flake8 .
```

3. Formatage :

```bash
black .
```

Dockerisation (création d'une image de ton app) :

1. Installation Docker :

Sur Linux (Ubuntu) :

```bash
sudo apt update
sudo apt install docker.io
sudo apt install docker-compose-plugin
sudo systemctl start docker
sudo systemctl enable docker
# Vérifier
docker --version

```

2. Création d'un fichier Dockerfile à la racine du projet 

Dockerfile permet de créer l'image.

```bash
# Utilise Python 3.10
FROM python:3.10

# Crée un dossier pour ton app
WORKDIR /app

# Copie requirements.txt et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout ton projet dans le conteneur
COPY . .

# Lancer FastAPI avec uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

3. Construction de l’image Docker manuellement (en local) 

```bash
docker build -t california-price-predictor .
```

Verification que FastAPI tourne :

4. Vérification de l'image :
```bash
docker images
```
5. Lancement du conteneur 
Si le fichier Dockerfile est déjà défini alors on exécute la commande :
```bash
docker run -p 8000:8000 california-price-predictor
```
La commande suivante exécute les deux commandes (3. et 5.) :
```bash
docker-compose up --build
```


Supprimer un image :
```bash
docker rmi <image_ID>
```
Supprimer toutes les images inutilisées :
```bash
docker image prune -a

```

6. Tester l’API :
```bash
http://localhost:8000/docs
```

7. Arrêter le conteneur :
Si tu veux arrêter le conteneur qui tourne en arrière-plan, d’abord liste les conteneurs :
```bash
docker ps
```
Puis arrête-le avec :

```bash
docker stop <container_id>
```

Supprimer un contenueur 
```bash
docker rm <container_id>
```

Arrêter proprement tous les conteneur
```bash
docker-compose down
```

- Une manière de 1ettoyer les anciennes images et conteneurs

Avant de lancer quoi que ce soit, assure-toi qu’il n’y a pas de conflit :

```bash
# Arrêter tous les conteneurs en cours
docker stop $(docker ps -aq)

# Supprimer tous les conteneurs
docker rm $(docker ps -aq)

# Supprimer toutes les images de ton projet (facultatif mais propre)
docker rmi -f $(docker images -q)
```

Parfois le port 8000 est utilisé par FastAPI et Streamlit en local alors qu'il n'y aucun conteneur qui tourne.
Le test en local de FastAPI et streamlit affichera un message d'erreur indiquant que le port 8000 est déjà utilisé.

Dans ce cas là, il faut identifier les service utilisant le port 800 avec la commande suivante :

```bash
sudo lsof -i :8000
```
Ensuite, il faut arrêter les processus qui utilisent le port 8000 :

```bash
sudo kill -9 PID
```

Création d'un docker-compose.yml :

Il permet d'automatiser la création d'une image et d'un conteneur dans environnement cloud

```bash
version: "3.9"

services:
  web:
    build: .
    container_name: california-price-predictor
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```

Vérifier la syntaxe

```bash
docker-compose config
```


Création d'un deuxieme Dockerfile "Dockerfile.streamlit" pour le service streamlit :
Render ne sait pas exécuter 2 serivces dans le même fichier Dockerfile.

```bash
FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# Render définit automatiquement $PORT
CMD ["sh", "-c", "streamlit run app/streamlit_app.py --server.port ${PORT:-8501} --server.address 0.0.0.0"]

```

✅ Tester en local Dockerfile.streamlit

1. Construction de l'image :

```bash
docker build -f Dockerfile.streamlit -t california-streamlit .
```
👉 -f Dockerfile.streamlit dit à Docker d’utiliser ce fichier au lieu de Dockerfile.

2/Lancement du conteneur :
```bash
docker run -p 8501:8501 california-streamlit
```

Tu exposes bien 8501 côté hôte et côté conteneur.
Ensuite, ouvre http://localhost:8501
Ton app Streamlit doit s’afficher.
=> aucun résultat ne sera affiché depuis la page web streamlit car le service FastAPI n'est pas lancé.
Pour tester correctement, il faut lancer les deux services au même temps avec la commande suivante :
```bash
docker-compose up --build
```



🚀 Étapes pour déployer FastAPI + Streamlit sur Render

1. Préparer les deux Dockerfile

Dockerfile (FastAPI)
Déjà en place, avec :
```bash
CMD ["sh", "-c", "uvicorn app.api:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

Dockerfile.streamlit (Streamlit) déjà créé ci-dessus à la racine du projet :


2. Vérifier en local avec Docker Compose

Avant Render, tu peux tester les deux services ensemble :

```bash
docker-compose down -v
docker-compose up --build
```
👉 Tu auras :

API dispo sur http://localhost:8000/docs
Streamlit dispo sur http://localhost:8501

3. Créer un dépôt GitHub propre

Ton .dockerignore doit ressembler à ça :

```bash
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.git
.gitignore
docker-compose.yml
```
⚠️ NE PAS mettre Dockerfile ni Dockerfile.streamlit dans .dockerignore, sinon Render ne les verra pas.


4. Créer un compte Render (déjà fait)

Connexion via GitHub. Donne accès à ton repo california-price-predictor.

5. Création d'un projet + 2 services dans Render

5. 1. Création projet Render

New -> Project
Nom : california-price-predictor

5. 2. Créer deux services Render
👉 Service 1 : FastAPI

New → Web Service

Repo : california-price-predictor

Branche : main

Environment : Docker

Dockerfile Path : Dockerfile

Context Directory : .

Type : Free

👉 Service 2 : Streamlit

New → Web Service

Repo : california-price-predictor-streamlit

Branche : feature/streamlit-deploy (ou main si tu as mergé)

Environment : Docker

Dockerfile Path : Dockerfile.streamlit

Context Directory : .

Type : Free

Rajouter dans Manage -> Environment -> Environment la variable : API_URL =https://california-price-predictor.onrender.com/predict
celà permettra d'exécuter streaml selon le contexte loal ou sur render.

6. Variables d’environnement

FastAPI : rien à ajouter (Render fournit déjà $PORT).

Streamlit : rien non plus, $PORT est géré automatiquement.

7. Déploiement automatique

Pour chaque service :

Render build l’image à partir du bon Dockerfile.

Il lance la commande CMD.

Tu vois le log → si pas d’erreurs, Your service is live 🎉

8. Tester en ligne

API FastAPI :
👉 https://california-price-predictor.onrender.com/docs

App Streamlit :
👉 https://california-price-predictor-streamlit.onrender.com

⚠️ Important : Dans ton streamlit_app.py, les appels à l’API doivent pointer vers l’URL Render de l’API (https://california-price-predictor.onrender.com/predict), et pas http://api:8000. 
Ce point est géré par la variable "API_URL =https://california-price-predictor.onrender.com/predict" qu'on a créé dans "Manage -> Environment -> Environment la variable".






Schésma simplifié :

```bash
┌───────────────────────────────┐
│       Ton dossier local        │
│   (app/, tests/, requirements) │
└───────────────┬───────────────┘
                │ COPY . .
                ▼
┌───────────────────────────────┐
│        Conteneur Docker        │
│        WORKDIR = /app          │
│   Tous les fichiers sont ici   │
└───────────────┬───────────────┘
                │ docker build -t california-price-predictor .
                ▼
┌───────────────────────────────┐
│         Image Docker           │
│ - Contient Python              │
│ - Contient dépendances         │
│ - Contient ton code et scripts │
└───────────────┬───────────────┘
                │ docker run
                ▼
┌───────────────────────────────┐
│      Conteneur en exécution   │
│ - Lancer ton API FastAPI      │
│ - Exécuter les tests          │
│ - Déployer sur un serveur     │
└───────────────────────────────┘

```

Schéma visuel PC -> Docker -> API -> Prédiction :

```bash

+---------------------+       +-------------------------+       +-----------------+
|                     |       |                         |       |                 |
|   Votre ordinateur  | <-->  |  Conteneur Docker       | <-->  |  API FastAPI    |
|   (localhost)       |       |  "california-price-    |       |  avec modèle    |
|                     |       |  predictor"             |       |  entraîné       |
+---------------------+       +-------------------------+       +-----------------+
          |                                |                             |
          | HTTP GET / POST                | Exécution des endpoints      |
          |-------------------------------->                             |
          |                                |                             |
          | <------------------------------|                             |
          |  JSON réponse (prediction)     |                             |
          |                                |                             |
```

Explication :

1°) Votre PC

-Tu envoies des requêtes HTTP (GET, POST) depuis le navigateur ou curl.

2°) Docker

-Conteneur isolé contenant tout ton projet Python + FastAPI.

-Il reçoit tes requêtes et les transmet à FastAPI.

3°) API FastAPI

-Expose les endpoints / et /predict.

-Charge le modèle et retourne la prédiction sous forme de JSON.

4°) Retour vers votre PC

- Docker envoie la réponse au navigateur ou terminal.

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
mkdir -p $PROJECT_NAME/{app,tests,.github/workflows}

# Création des fichiers dans app/
touch $PROJECT_NAME/app/__init__.py
touch $PROJECT_NAME/app/main.py
touch $PROJECT_NAME/app/streamlit_app.py
touch $PROJECT_NAME/app/model.py
touch $PROJECT_NAME/app/train.py
touch $PROJECT_NAME/app/schemas.py
touch $PROJECT_NAME/app/utils.py


# Tests
touch $PROJECT_NAME/tests/__init__.py
touch $PROJECT_NAME/tests/test_api.py
touch $PROJECT_NAME/tests/test_model.py
touch $PROJECT_NAME/tests/test_utils.py

# GitHub Actions (CI/CD)
touch $PROJECT_NAME/.github/workflows/python-tests.yml

# Fichiers racine
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/pytest.ini
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
│  ├─ api.py            # API FastAPI
│  ├─ model.py          # Chargement et prédiction du modèle
│  ├─ utils.py          # Fonctions utilitaires (prétraitement)
│  └─ streamlit_app.py  # Interface Streamlit
│
├─ scripts/
│  └─ train_model.py    # Script pour entraîner le modèle
├─ tests/
│  └─ ttest_api.py
├─ model.joblib         # Modèle entraîné (généré après exécution)
├─ requirements.txt     # Dépendances Python
├─ setup.sh             # Script d’initialisation du projet
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


## 🧠 Entraînement du modèle

Le modèle est basé sur Linear Regression pour prédire le prix médian des maisons.

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

le résultat devrait être :
{
  "prediction": 4.13164641129476
}
```

## 🌐 Interface Streamlit

**1.** Lancer Streamlit :
```bash
streamlit run app/streamlit_app.py
```
Si un message d'erreur lié à protobuf, il y'a une solution de contournement qui permet d'exporter ka variable d'environnement (exécute cette dernière commande d'abord):
**1.** Lancer Streamlit :
```bash
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```


**2.** L’interface web sera accessible ici :
```bash
http://localhost:8501
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


## ⚙️ Dépendances principales

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
    Assurez-vous que l’environnement virtuel actif correspond à celui utilisé pour installer les dépendances.

    Si le modèle model.joblib a été généré avec une autre version de Python, supprimez-le et réentraînez-le avec votre version actuelle.

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

Tests API

- test_root_endpoint → Vérifie que / fonctionne.

- test_predict_valid_data → Vérifie une prédiction avec de bonnes données.

- test_predict_invalid_data → Vérifie qu’une donnée invalide renvoie bien une erreur 422.

- test_predict_missing_field → Vérifie qu’un champ manquant renvoie une erreur 422.

Tests Modèle

- test_model_loads → Vérifie que le modèle est bien chargé.

- test_model_prediction_float → Vérifie qu’une prédiction renvoie bien un float.

- test_model_prediction_reproducibility → Vérifie que deux prédictions identiques donnent le même résultat.


Tests, lightings et formatage :

1. Lancer les tests :
```bash
pytest tests/ --maxfail=1 --disable-warnings -v
```

2. Vérification le linting et le formatage 

```bash
black --check .
flake8 .
```

3. Formatage :

```bash
black .
```

Dockerisation (création d'une image de ton app)

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

Verification que FastAPI tourne dans DOCKER :

4. Vérification de l'image :
```bash
docker images
```
5. Lancement du conteneur 
Si le fichier Dockerfile est déjà défini alors on exécute la commande :
```bash
docker run -p 8000:8000 -p 8501:8501 california-price-predictor
```
La commande suivante exécute celle définies ans le point 3. et 5. :
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
http://localhost:8000

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

Supprimer un contenuer 
```bash
docker rm <container_id>

```

Parfois le port 8000 est utilisé par FastAPI et Streamlit en local alors que il n'y aucun conteneur quin tourne.
Le test en local de FastAPI et streamlit affichera un message d'erreur indiquant que le port 8000 est déjà utilisé.
Dans ce cas là, il faut identifier les service utilisant le port 800 avec la commande suivante :
```bash
sudo lsof -i :8000
```
Ensuite, il faut arrêter les processus qui utilisent le port 8000 :

```bash
sudo kill -9 PID
```


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




Sauvegarde et recharge d'une image Docker :

1. Sauvegarde :

Supposons que l'image "california-price-predictor" est déjà construite :

```bash
docker save -o california-price-predictor.tar california-price-predictor:latest

```

2 Recharge 

```bash
docker load -i california-price-predictor.tar
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

Construire les images (sans exécuter)


Lancer en mode détaché :

Démarre les conteneurs en arrière-plan.
```bash
docker-compose up -d
```
voir l’état avec :

```bash
docker-compose ps
```

Tester l’application
```bash
http://localhost:8000/docs
```

Arrêter proprement
```bash
docker-compose down
```


1️⃣ Nettoyer les anciennes images et conteneurs

Avant de lancer quoi que ce soit, assure-toi qu’il n’y a pas de conflit :

```bash
# Arrêter tous les conteneurs en cours
docker stop $(docker ps -aq)

# Supprimer tous les conteneurs
docker rm $(docker ps -aq)

# Supprimer toutes les images de ton projet (facultatif mais propre)
docker rmi -f $(docker images -q)


```


Création d'un deuxieme Dockerfile "Dockerfile.streamlit" pour le service streamlit :
Render ne sait pas exécuter 2 serivces dans le mê fichier Dockerfile.

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
1. COnstruction de l'image :

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

Dockerfile.streamlit (Streamlit)
À créer à la racine du projet :
```bash
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render définit automatiquement $PORT → on s'y connecte
CMD ["sh", "-c", "streamlit run app/streamlit_app.py --server.port $PORT --server.address 0.0.0.0"]

```

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

5. Créer deux services Render
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

Repo : california-price-predictor

Branche : feature/streamlit-deploy (ou main si tu as mergé)

Environment : Docker

Dockerfile Path : Dockerfile.streamlit

Context Directory : .

Type : Free

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
👉 https://california-price-predictor-1.onrender.com

⚠️ Important : Dans ton streamlit_app.py, les appels à l’API doivent pointer vers l’URL Render de l’API (https://california-price-predictor.onrender.com/predict), et pas http://api:8000.
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
│  ├─ train_model.py    # Entraînement et sauvegarde du modèle
│  └─ streamlit_app.py  # Interface Streamlit
│
├─ scripts/
│  └─ train_model.py    # Script pour entraîner le modèle
│
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

Cela sauvegardera le modèle entraîné dans model.joblib.


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

**2.** L’interface web sera accessible ici :
```bash
http://localhost:8502
```


## 📓 Utiliser Jupyter Notebooks pour l’analyse exploratoire

**1.**Installer Jupyter si ce n’est pas déjà fait :
    
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

Python 3.10+

scikit-learn

pandas

numpy

fastapi

uvicorn

streamlit

joblib

pydantic
```

## 📌 Notes
```bash
    Assurez-vous que l’environnement virtuel actif correspond à celui utilisé pour installer les dépendances.

    Si le modèle model.joblib a été généré avec une autre version de Python, supprimez-le et réentraînez-le avec votre version actuelle.
```
import joblib
import os
from sklearn.linear_model import LinearRegression

def train_model(X, y):
    """Entraîne un modèle de régression linéaire et le renvoie."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def save_model(model, filename="model.joblib"):
    """Sauvegarde le modèle dans le dossier racine du projet."""
    path = os.path.join(os.path.dirname(__file__), "..", filename)
    joblib.dump(model, path)
    print(f"Modèle sauvegardé dans {path}")

def load_model(filename="model.joblib"):
    """Charge le modèle sauvegardé."""
    path = os.path.join(os.path.dirname(__file__), "..", filename)
    return joblib.load(path)


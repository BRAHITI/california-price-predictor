import joblib
from sklearn.linear_model import LinearRegression

MODEL_PATH = "model.joblib"

def train_model(X, y):
    """Entraîne et retourne un modèle LinearRegression"""
    model = LinearRegression()
    model.fit(X, y)
    return model

def save_model(model, path=MODEL_PATH):
    joblib.dump(model, path)

def load_model(path=MODEL_PATH):
    return joblib.load(path)

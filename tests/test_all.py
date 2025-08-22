import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from app.api import app
from app.model import load_model
import numpy as np
from sklearn.linear_model import LinearRegression


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)

# -------------------------------
# Tests API
# -------------------------------
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "fonctionne" in response.json()["message"]

def test_predict_valid_data():
    data = {
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveRooms": 6.9841,
        "AveBedrms": 1.0238,
        "Population": 322.0,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    prediction = response.json()["prediction"]
    assert isinstance(prediction, float)

def test_predict_invalid_data():
    # Données invalides : AveRooms est une string
    data = {
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveRooms": "abc",
        "AveBedrms": 1.0238,
        "Population": 322.0,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
    response = client.post("/predict", json=data)
    # FastAPI renvoie une erreur 422 pour données invalides
    assert response.status_code == 422

def test_predict_missing_field():
    # Données manquantes : pas de AveRooms
    data = {
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveBedrms": 1.0238,
        "Population": 322.0,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 422

# -------------------------------
# Tests modèle
# -------------------------------
def test_model_loads():
    model = load_model()
    assert isinstance(model, LinearRegression)

def test_model_prediction_float():
    model = load_model()
    X = np.array([[8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]])
    prediction = model.predict(X)[0]
    assert isinstance(prediction, float)

def test_model_prediction_reproducibility():
    model = load_model()
    X = np.array([[8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]])
    pred1 = model.predict(X)[0]
    pred2 = model.predict(X)[0]
    assert pred1 == pytest.approx(pred2)  # prédictions identiques

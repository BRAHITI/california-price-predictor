import sys, os

# Ajouter le chemin du projet pour trouver app.model
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import numpy as np
from sklearn.linear_model import LinearRegression

from app.model import load_model


def test_model_loads():
    """Vérifie que le modèle est bien chargé"""
    model = load_model()
    assert isinstance(model, LinearRegression)


def test_model_prediction_float():
    """Vérifie que le modèle renvoie bien un float"""
    model = load_model()
    X = np.array([[8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]])
    prediction = model.predict(X)[0]
    assert isinstance(prediction, float)


def test_model_prediction_reproducibility():
    """Vérifie que le modèle est déterministe"""
    model = load_model()
    X = np.array([[8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]])
    pred1 = model.predict(X)[0]
    pred2 = model.predict(X)[0]
    assert pred1 == pytest.approx(pred2)  # même résultat attendu

# tests/test_api.py
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.api import app
from fastapi.testclient import TestClient


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)


def test_predict_endpoint():
    # Exemple de données correctes
    data = {
        "MedInc": 8.3252,
        "HouseAge": 41.0,
        "AveRooms": 6.9841,
        "AveBedrms": 1.0238,
        "Population": 322.0,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23,
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()

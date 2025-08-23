import numpy as np
from app.model import load_model


def test_model_loads():
    model = load_model()
    assert model is not None


def test_model_prediction():
    model = load_model()
    X = np.array([[8.3252, 41.0, 6.9841, 1.0238, 322.0, 2.5556, 37.88, -122.23]])
    pred = model.predict(X)
    assert len(pred) == 1
    assert isinstance(pred[0], float)

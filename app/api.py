from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model

app = FastAPI()

# Charger le modèle une seule fois au démarrage
model = load_model()


# Modèle de données pour POST
class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


# Route GET pour tester si l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "API FastAPI fonctionne !"}


# Route POST pour prédiction
@app.post("/predict")
def predict(data: HouseData):
    X = [
        [
            data.MedInc,
            data.HouseAge,
            data.AveRooms,
            data.AveBedrms,
            data.Population,
            data.AveOccup,
            data.Latitude,
            data.Longitude,
        ]
    ]
    prediction = model.predict(X)[0]
    return {"prediction": prediction}

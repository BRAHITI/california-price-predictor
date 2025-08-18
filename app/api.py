from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model
from app.utils import create_dataframe_from_dict, preprocess_data

app = FastAPI()
model = load_model()

class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict")
def predict(data: HouseData):
    df = create_dataframe_from_dict(data.dict())
    df = preprocess_data(df)
    prediction = model.predict(df)
    return {"prediction": prediction[0]}

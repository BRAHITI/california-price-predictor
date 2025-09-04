import streamlit as st
import requests

# import os pour l'utilisation de l'une des deux valeur de API_URL selon qu'on est en local ou dans render
import os

# ajout de cette variale selon l'environnement local ou render
API_URL = os.getenv("API_URL", "http://api:8000/predict")  # par défaut local

st.title("Prédiction du prix des maisons en Californie")

# Inputs utilisateur
MedInc = st.number_input("MedInc")
HouseAge = st.number_input("HouseAge")
AveRooms = st.number_input("AveRooms")
AveBedrms = st.number_input("AveBedrms")
Population = st.number_input("Population")
AveOccup = st.number_input("AveOccup")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Prédire"):
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude,
    }
    # remplacement de l'URL en dur par la variable API_URL
    #response = requests.post("http://api:8000/predict", json=data)
    response = requests.post(API_URL, json=data)
    st.success(f"Prix prédit : {response.json()['prediction']:.3f} (en dizaines de milliers de $)")

    # Dans ton service Streamlit → Settings → Environment → Add Environment Variable :
    #API_URL=https://california-price-predictor.onrender.com/predict

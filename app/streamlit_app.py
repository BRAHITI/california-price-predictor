import streamlit as st
import requests

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
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    st.success(
        f"Prix prédit : {response.json()['prediction']:.3f} (en dizaines de milliers de $)"
    )

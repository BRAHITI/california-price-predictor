import pandas as pd
from sklearn.preprocessing import StandardScaler

def create_dataframe_from_dict(data_dict):
    """Crée un DataFrame à partir d'un dictionnaire pour prédiction"""
    return pd.DataFrame([data_dict])

def preprocess_data(df):
    """Préprocessing éventuel (placeholder pour scaler ou features)"""
    # Exemple : StandardScaler si besoin
    # scaler = StandardScaler()
    # return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df

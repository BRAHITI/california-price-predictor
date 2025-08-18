from sklearn.datasets import fetch_california_housing
from app.model import train_model, save_model
from app.utils import preprocess_data

# Charger le dataset
data = fetch_california_housing(as_frame=True)
X = preprocess_data(data.data)
y = data.target

# Entraîner le modèle
model = train_model(X, y)

# Sauvegarder le modèle
save_model(model)
print("Modèle entraîné et sauvegardé !")



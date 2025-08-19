from sklearn.datasets import fetch_california_housing
from app.model import train_model, save_model
from app.utils import preprocess_data
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, r2_score


# Charger le dataset
data = fetch_california_housing(as_frame=True)
X = preprocess_data(data.data)
y = data.target
# Split train/test avec random_state pour reproductibilité
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Entraîner le modèle
model = train_model(X_train, y_train)

# prédictions sur le test set
y_pred = model.predict(X_test)

# calcul des métriques
#rmse = mean_squared_error(y_test, y_pred, squared=False)
mse=mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")


# Sauvegarder le modèle
save_model(model)
print("Modèle entraîné et sauvegardé !")



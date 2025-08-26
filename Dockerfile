# Utilise Python 3.10
FROM python:3.10

# Crée un dossier pour ton app
WORKDIR /app

# Copie requirements.txt et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout ton projet dans le conteneur
COPY . .

# Lancer FastAPI avec uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
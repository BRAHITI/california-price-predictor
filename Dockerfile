FROM python:3.10

# Eviter pycache + buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

# Ancienne commande pour Dockerfile pour les tests en local et ave docker-compose.yml
#CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]

# Nouvelle commande pour Dockerfile pour le déploiement dans render
CMD ["sh", "-c", "uvicorn app.api:app --host 0.0.0.0 --port ${PORT:-8000}"]


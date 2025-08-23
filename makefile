.PHONY: lint format test

# Vérifie le style sans modifier
lint:
	flake8 .
	black --check .

# Corrige automatiquement le style avec Black
format:
	black .

# Lancer tous les tests
test:
	pytest -v
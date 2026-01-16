# Flask API - Pipeline CI

Application Flask avec pipeline CI utilisant GitHub Actions.

## Structure du projet

```
.
├── api.py              # Application Flask
├── db.py              # Gestion de la base de données SQLite
├── utils.py           # Fonctions utilitaires
├── requirements.txt   # Dépendances Python
├── tests/             # Tests unitaires
│   └── test_api.py
└── .github/
    └── workflows/
        └── ci.yml     # Pipeline d'intégration continue
```

## Pipeline CI (Intégration Continue)

Le workflow CI (`.github/workflows/ci.yml`) se déclenche automatiquement sur la branche `tp2` :

**Actions automatiques** :
- Vérification du code avec Ruff (linting)
- Vérification des types avec mypy
- Analyse de complexité avec Radon
- Exécution des tests avec pytest et génération de coverage
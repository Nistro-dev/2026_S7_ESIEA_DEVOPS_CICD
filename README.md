# Flask API - Pipeline CI/CD & Kubernetes

Application Flask avec pipeline CI/CD complet utilisant GitHub Actions, containerisation Docker, et déploiement Kubernetes.

## Description

API REST développée avec Flask permettant la gestion d'utilisateurs et le traitement de données. L'application utilise SQLite comme base de données, est containerisée avec Docker, et dispose de manifestes Kubernetes générés automatiquement pour un déploiement en production.

## Fonctionnalités

- **API REST** : Endpoints de gestion d'utilisateurs (CRUD)
- **Base de données** : SQLite avec gestion automatique des migrations
- **Tests automatisés** : Suite de tests avec pytest (6 tests, 91% coverage)
- **Qualité du code** : Linting (Ruff), type checking (mypy), analyse de complexité (Radon)
- **Containerisation** : Docker avec healthcheck
- **Registry** : Images Docker publiées sur GitHub Container Registry (GHCR)
- **Kubernetes** : Manifestes générés automatiquement avec Kompose
- **CI/CD automatique** : GitHub Actions avec déploiement FTP

## Structure du projet

```
.
├── api.py              # Application Flask avec endpoints REST
├── db.py              # Gestion de la base de données SQLite
├── utils.py           # Fonctions utilitaires
├── requirements.txt   # Dépendances Python
├── Dockerfile         # Image Docker
├── docker-compose.yml # Configuration Docker Compose avec healthcheck
├── pytest.ini         # Configuration pytest
├── tests/             # Tests unitaires
│   └── test_api.py    # 6 tests (health, users CRUD, dothing)
└── .github/
    └── workflows/
        └── ci-cd.yml  # Pipeline CI/CD complet
```

## Pipeline CI/CD

Le workflow (`.github/workflows/ci-cd.yml`) se déclenche automatiquement sur la branche `tp2` et comporte 4 jobs séquentiels :

### 1. Lint & Test
- Vérification du code avec Ruff (linting)
- Vérification des types avec mypy
- Analyse de complexité avec Radon
- Exécution des tests avec pytest (coverage 91%)

### 2. Docker Test
- Build de l'image Docker
- Démarrage des services avec docker-compose
- Vérification du healthcheck
- Tests de santé du conteneur

### 3. Build & Push Image
- Build de l'image Docker
- Tag automatique avec branch + commit SHA
- Publication sur GitHub Container Registry (GHCR)
- Image disponible : `ghcr.io/nistro-dev/2026_s7_esiea_devops_cicd/flask-api:tp2-<SHA>`

### 4. Generate Manifests & Deploy
- Installation de Kompose
- Génération automatique des manifestes Kubernetes
- Création de l'archive `MichaudMaelPython.zip` contenant :
  - Manifestes Kubernetes (Deployment, Service, PVC)
  - docker-compose.yml
  - README.md
- Upload via FTP vers `RenduDevopsKube/`
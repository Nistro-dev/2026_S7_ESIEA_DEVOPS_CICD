import pytest
import os
import tempfile
from api import create_app
from db import init_db

@pytest.fixture
def app():
    # Créer une base de données temporaire pour les tests
    db_fd, db_path = tempfile.mkstemp()
    os.environ["APP_DB_PATH"] = db_path
    
    init_db()
    app = create_app()
    app.config["TESTING"] = True
    
    yield app
    
    # Cleanup
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_endpoint(client):
    """Test que l'endpoint health renvoie ok"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_create_user(client):
    """Test la création d'un utilisateur"""
    response = client.post("/users", json={"name": "Alice"})
    assert response.status_code == 201
    assert "id" in response.json
    assert isinstance(response.json["id"], int)

def test_get_user(client):
    """Test la récupération d'un utilisateur"""
    # Créer un utilisateur d'abord
    create_response = client.post("/users", json={"name": "Bob"})
    user_id = create_response.json["id"]
    
    # Récupérer l'utilisateur
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json["id"] == user_id
    assert response.json["name"] == "Bob"

def test_get_user_not_found(client):
    """Test la récupération d'un utilisateur inexistant"""
    response = client.get("/users/99999")
    assert response.status_code == 404
    assert response.json == {"error": "not found"}

def test_dothing_endpoint(client):
    """Test l'endpoint dothing avec des données valides"""
    response = client.post("/dothing", json={
        "name": "test",
        "meta": [1, 2, 3, 4, 5, 6, 7, 8, 9]
    })
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_dothing_invalid_meta(client):
    """Test l'endpoint dothing avec des métadonnées invalides"""
    response = client.post("/dothing", json={
        "name": "test",
        "meta": [1, 2, 3]  # Pas assez de valeurs
    })
    assert response.status_code == 400
    assert "meta must be a list of 9 values" in response.json["error"]

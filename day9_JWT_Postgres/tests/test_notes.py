from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():

    response = client.post(
        "/auth/login",
        json={
            "username": "pytest_user",
            "password": "pytest123"
        }
    )

    return response.json()["access_token"]

def test_create_note():

    token = get_token()

    response = client.post(
        "/notes",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Testing",
            "content": "Pytest"
        }
    )

    assert response.status_code == 200

def test_get_notes():

    token = get_token()

    response = client.get(
        "/notes",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)

def test_invalid_login():

    response = client.post(
        "/auth/login",
        json={
            "username": "wrong",
            "password": "wrong"
        }
    )

    assert response.status_code == 401

def test_notes_without_token():

    response = client.get("/notes")

    assert response.status_code == 403
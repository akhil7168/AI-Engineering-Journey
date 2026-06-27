from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register():
    response = client.post(
        "/auth/register",
        json={
            "username": "pytest_user",
            "password": "pytest123"
        }
    )

    assert response.status_code in [200, 400]

def test_login():

    response = client.post(
        "/auth/login",
        json={
            "username": "pytest_user",
            "password": "pytest123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
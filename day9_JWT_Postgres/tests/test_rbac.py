from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)


def register_user(username, password):
    return client.post(
        "/auth/register",
        json={
            "username": username,
            "password": password
        }
    )


def login_user(username, password):
    response = client.post(
        "/auth/login",
        json={
            "username": username,
            "password": password
        }
    )

    print(response.status_code)
    print(response.json())

    return response.json()["access_token"]


def test_normal_user_cannot_access_admin():
    username = "normaluser"
    password = "password123"

    # Register only if the user doesn't already exist
    register_response = register_user(username, password)

    if register_response.status_code not in (200, 400):
        assert False, register_response.json()

    token = login_user(username, password)

    response = client.get(
        "/admin",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Admin access required"


def test_admin_endpoint_without_token():
    response = client.get("/admin")

    # HTTPBearer returns 401 when Authorization header is missing
    assert response.status_code == 401


@pytest.mark.skip(reason="Admin user creation is not implemented yet")
def test_admin_can_access_dashboard():
    """
    This test will be enabled once an admin account
    creation workflow is implemented.
    """
    token = login_user("admin", "adminpassword")

    response = client.get(
        "/admin",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome Admin"
    }
import sys
import os
from fastapi.testclient import TestClient

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from app.main import app

client = TestClient(app)


def test_login_success():
    """
    Test for user login success
    """
    payload = {
        "username": "newuser",
        "password": "hashed_password"
    }

    response = client.post(
        '/auth/login',
        json=payload
    )

    assert response.status_code == 200
    assert response.json()['message'] == "Login successful"


def test_login_invalid_username():
    """
    Test for incorrect username
    """
    payload = {
        "username": "invaliduser",
        "password": "hashed_password"
    }

    response = client.post(
        '/auth/login',
        json=payload
    )
    assert response.status_code == 400
    assert response.json()['detail'] == "Invalid username or password"


def test_login_invalid_password():
    """
    Test for incorrect password
    """
    payload = {
        "username": "testuser",
        "password": "wrong_password"
    }

    response = client.post(
        '/auth/login',
        json=payload
    )
    assert response.status_code == 400
    assert response.json()['detail'] == "Invalid username or password"

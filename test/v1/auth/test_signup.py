import sys
import os
from fastapi.testclient import TestClient

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from app.main import app

client = TestClient(app)


def test_signup_success():
    """
    Test for signup success
    """
    payload = {
        "username": "newtestuser10",
        "password": "hashed_password"
    }

    response = client.post(
        '/auth/signup',
        json=payload
    )

    assert response.status_code == 200
    assert response.json()['message'] == "User created successfully"


def test_signup_existing_username():
    """
    Test for signup with existing user
    """
    payload = {
        "username": "newtestuser",
        "password": "new_password"
    }

    response = client.post(
        '/auth/signup',
        json=payload
    )

    assert response.status_code == 400
    assert response.json()['detail'] == "Username already exist"

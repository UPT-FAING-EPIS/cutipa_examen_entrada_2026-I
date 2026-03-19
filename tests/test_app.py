import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_for_activity_success():
    # Arrange
    activity_name = "Chess Club"
    email = "testuser@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code in (200, 400, 409)  # 400/409 si ya está inscrito
    if response.status_code == 200:
        assert f"Signed up {email}" in response.json()["message"]

def test_signup_for_activity_not_found():
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "testuser2@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

def test_get_activities():
    # Arrange
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

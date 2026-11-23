from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_user_crud():
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"

    # Create user
    response = client.post("/users", json={
        "first_name": "Test",
        "last_name": "User",
        "email": email
    })
    assert response.status_code == 200
    user_id = response.json()["id"]

    # Get user by ID
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == email

    # Update user
    response = client.put(f"/users/{user_id}", json={
        "first_name": "Updated",
        "last_name": "User",
        "email": email
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Updated"

    # Delete user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
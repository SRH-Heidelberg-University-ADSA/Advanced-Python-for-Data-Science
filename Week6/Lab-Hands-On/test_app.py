# Import the Flask application for testing.
from app import app


# Test that the home endpoint returns HTTP 200.
def test_home_returns_200():
    # Create a test client to send requests to the Flask app.
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


# Test that the home endpoint returns a message field.
def test_home_contains_message():
    client = app.test_client()

    response = client.get("/")

    assert "message" in response.get_json()


# Test that the health endpoint returns the expected status.
def test_health_returns_ok():
    client = app.test_client()

    response = client.get("/health")

    assert response.get_json()["status"] == "ok"
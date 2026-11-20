
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running"

def test_profile_endpoint():
    response = client.get("/profile")
    assert response.status_code == 200
    assert response.json()["total_transactions"] == 7

def test_duplicate_detection():
    response = client.get("/profile")
    data = response.json()
    assert "T002" in data["duplicate_transaction_ids"]

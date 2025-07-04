import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Wimbledon Tournament Service"}

def test_get_wimbledon_final_success():
    response = client.get("/wimbledon/?year=2021")
    assert response.status_code == 200
    data = response.json()
    assert data["year"] == 2021
    assert data["champion"] == "Novak Djokovic"
    assert data["runner_up"] == "Matteo Berrettini"
    assert data["sets"] == 4
    assert data["tiebreak"] is True

def test_get_wimbledon_final_not_found():
    response = client.get("/wimbledon/?year=1999")
    assert response.status_code == 404
    assert "No Wimbledon final data found for year 1999" in response.text

def test_get_wimbledon_final_invalid_year():
    response = client.get("/wimbledon/?year=notanumber")
    assert response.status_code == 422 
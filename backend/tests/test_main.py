from fastapi.testclient import TestClient
from ..backend import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message:": "Welcome to our API page!"}

def test_predict_cancer():
    # Mock input data with correct structure
    input_data = {
        "features": [5, 6, 7, 4, 3, 8, 2, 6, 1]  # Replace with realistic values
    }
    response = client.post("/predict/", json=input_data)
    
    # Assert the response status code
    assert response.status_code == 200
    
    # Assert the response contains a class name
    assert "class" in response.json()
    assert isinstance(response.json()["class"], str)
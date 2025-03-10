from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sum_endpoint_valid():
    response = client.post("/api/v1/sum/", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"sum": 6}

def test_sum_endpoint_empty_list():
    response = client.post("/api/v1/sum/", json={"numbers": []})
    assert response.status_code == 422
    assert "A lista de números não pode estar vazia." in response.text

def test_sum_endpoint_negative_numbers():
    response = client.post("/api/v1/sum/", json={"numbers": [1, -2, 3]})
    assert response.status_code == 422
    assert "Todos os números devem ser positivos." in response.text

def test_sum_endpoint_too_many_elements():
    response = client.post("/api/v1/sum/", json={"numbers": list(range(101))})
    assert response.status_code == 422
    assert "A lista de números não pode ter mais de 100 elementos." in response.text

def test_average_endpoint_valid():
    response = client.post("/api/v1/average/", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"average": 2.0}

def test_average_endpoint_empty_list():
    response = client.post("/api/v1/average/", json={"numbers": []})
    assert response.status_code == 422
    assert "A lista de números não pode estar vazia." in response.text

def test_average_endpoint_negative_numbers():
    response = client.post("/api/v1/average/", json={"numbers": [1, -2, 3]})
    assert response.status_code == 422
    assert "Todos os números devem ser positivos." in response.text

def test_average_endpoint_too_many_elements():
    response = client.post("/api/v1/average/", json={"numbers": list(range(101))})
    assert response.status_code == 422
    assert "A lista de números não pode ter mais de 100 elementos." in response.text

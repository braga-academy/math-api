from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sum_endpoint_valid():
    # Testa o endpoint /sum/ com uma lista válida de números
    response = client.post("/api/v1/sum/", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"sum": 6}

def test_sum_endpoint_empty_list():
    # Testa o endpoint /sum/ com uma lista vazia
    response = client.post("/api/v1/sum/", json={"numbers": []})
    assert response.status_code == 422  # Unprocessable Entity
    assert "A lista de números não pode estar vazia." in response.text

def test_sum_endpoint_negative_numbers():
    # Testa o endpoint /sum/ com números negativos
    response = client.post("/api/v1/sum/", json={"numbers": [1, -2, 3]})
    assert response.status_code == 422  # Unprocessable Entity
    assert "Todos os números devem ser positivos." in response.text

def test_sum_endpoint_too_many_elements():
    # Testa o endpoint /sum/ com mais de 100 elementos
    response = client.post("/api/v1/sum/", json={"numbers": list(range(101))})
    assert response.status_code == 422  # Unprocessable Entity
    assert "A lista de números não pode ter mais de 100 elementos." in response.text

def test_average_endpoint_valid():
    # Testa o endpoint /average/ com uma lista válida de números
    response = client.post("/api/v1/average/", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"average": 2.0}

def test_average_endpoint_empty_list():
    # Testa o endpoint /average/ com uma lista vazia
    response = client.post("/api/v1/average/", json={"numbers": []})
    assert response.status_code == 422  # Unprocessable Entity
    assert "A lista de números não pode estar vazia." in response.text

def test_average_endpoint_negative_numbers():
    # Testa o endpoint /average/ com números negativos
    response = client.post("/api/v1/average/", json={"numbers": [1, -2, 3]})
    assert response.status_code == 422  # Unprocessable Entity
    assert "Todos os números devem ser positivos." in response.text

def test_average_endpoint_too_many_elements():
    # Testa o endpoint /average/ com mais de 100 elementos
    response = client.post("/api/v1/average/", json={"numbers": list(range(101))})
    assert response.status_code == 422  # Unprocessable Entity
    assert "A lista de números não pode ter mais de 100 elementos." in response.text

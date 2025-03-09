import pytest
from app.models.numbers import NumbersRequest
from pydantic import ValidationError

def test_numbers_request_valid():
    # Testa uma lista válida
    request = NumbersRequest(numbers=[1, 2, 3])
    assert request.numbers == [1, 2, 3]

def test_numbers_request_empty_list():
    # Testa uma lista vazia
    with pytest.raises(ValidationError) as exc_info:
        NumbersRequest(numbers=[])
    assert "A lista de números não pode estar vazia." in str(exc_info.value)

def test_numbers_request_too_many_elements():
    # Testa uma lista com mais de 100 elementos
    with pytest.raises(ValidationError) as exc_info:
        NumbersRequest(numbers=list(range(101)))
    assert "A lista de números não pode ter mais de 100 elementos." in str(exc_info.value)

def test_numbers_request_negative_numbers():
    # Testa uma lista com números negativos
    with pytest.raises(ValidationError) as exc_info:
        NumbersRequest(numbers=[1, -2, 3])
    assert "Todos os números devem ser positivos." in str(exc_info.value)

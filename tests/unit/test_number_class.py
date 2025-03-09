import pytest
from app.models.numbers import Number

def test_number_sum():
    assert Number.sum(1, 2) == 3

def test_number_sum_large_numbers():
    assert Number.sum(1000000, 2000000) == 3000000

def test_number_divide():
    assert Number.divide(4, 2) == 2.0

def test_number_divide_decimal_result():
    assert Number.divide(5, 2) == 2.5

def test_number_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        Number.divide(4, 0)
    assert "Não é possível dividir por zero" in str(exc_info.value)

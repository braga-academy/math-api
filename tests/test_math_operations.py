import pytest
from app.models.numbers import Numbers, Number

def test_sum_numbers():
    assert Numbers.sum([1, 2, 3]) == 6

def test_average_numbers():
    assert Numbers.average([1, 2, 3]) == 2.0

def test_number_sum():
    assert Number.sum(1, 2) == 3

def test_number_divide():
    assert Number.divide(4, 2) == 2.0
    with pytest.raises(ValueError):
        Number.divide(4, 0)

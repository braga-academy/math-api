import pytest
from app.models.numbers import Numbers

def test_sum_numbers():
    assert Numbers.sum([1, 2, 3]) == 6

def test_sum_numbers_single_element():
    assert Numbers.sum([42]) == 42

def test_sum_numbers_large_list():
    assert Numbers.sum(list(range(1, 101))) == 5050  # Soma dos números de 1 a 100

def test_average_numbers():
    assert Numbers.average([1, 2, 3]) == 2.0

def test_average_numbers_single_element():
    assert Numbers.average([42]) == 42.0

def test_average_numbers_empty_list():
    assert Numbers.average([]) == 0.0  # Comportamento esperado para lista vazia

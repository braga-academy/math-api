from app.models.numbers import Numbers, Number

def sum_numbers(numbers: list[int]) -> int:
    return Numbers.sum(numbers)

def calculate_average(numbers: list[int]) -> float:
    return Numbers.average(numbers)

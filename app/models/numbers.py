from pydantic import BaseModel, Field, field_validator
from typing import List

class NumbersRequest(BaseModel):
    numbers: List[int] = Field(..., json_schema_extra={"example": [1, 2, 3]}, description="Lista de números inteiros.")

    @field_validator('numbers')
    def validate_numbers(cls, value):
        if not value:
            raise ValueError("A lista de números não pode estar vazia.")
        if len(value) > 100:
            raise ValueError("A lista de números não pode ter mais de 100 elementos.")
        for number in value:
            if number < 0:
                raise ValueError("Todos os números devem ser positivos.")
        return value

class Numbers:
    @staticmethod
    def sum(numbers: List[int]) -> int:
        return sum(numbers)

    @staticmethod
    def average(numbers: List[int]) -> float:
        return sum(numbers) / len(numbers) if numbers else 0

class Number:
    @staticmethod
    def sum(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def divide(a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

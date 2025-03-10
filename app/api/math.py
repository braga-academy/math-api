from fastapi import APIRouter, HTTPException, status
from aiocache import cached
from app.models.numbers import NumbersRequest
from app.services.math_operations import sum_numbers, calculate_average

router = APIRouter()

@router.post("/sum/", summary="Somar números", description="Recebe uma lista de números e retorna a soma.", tags=["Operações Matemáticas"])
@cached(ttl=60)
async def sum_endpoint(numbers_request: NumbersRequest):
    return {"sum": sum_numbers(numbers_request.numbers)}

@router.post("/average/", summary="Calcular média", description="Recebe uma lista de números e retorna a média aritmética.", tags=["Operações Matemáticas"])
@cached(ttl=60)
async def average_endpoint(numbers_request: NumbersRequest):
    try:
        return {"average": calculate_average(numbers_request.numbers)}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

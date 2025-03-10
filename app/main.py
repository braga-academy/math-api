from fastapi import FastAPI
from aiocache import RedisCache, cached
from aiocache.serializers import JsonSerializer
import os

from app.api.math import router as math_router
from app.api.health import router as health_router

app = FastAPI(
    title="Calc API",
    description="API para realizar operações matemáticas de soma e média.",
    version="1.0.0",
)

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

cache = RedisCache(endpoint="localhost", port=6379, namespace="fastapi-cache", serializer=JsonSerializer())

@app.get("/")
async def root():
    return {
        "message": "Bem-vindo à Calc API!",
        "documentation": {
            "swagger": "http://localhost:8000/docs",
            "redoc": "http://localhost:8000/redoc"
        }
    }

app.include_router(math_router, prefix="/api/v1")
app.include_router(health_router, prefix="/api/v1")

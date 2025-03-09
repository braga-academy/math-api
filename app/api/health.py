from fastapi import APIRouter

router = APIRouter()

@router.get("/health/", summary="Verificar status da API", tags=["Status"])
async def health_check():
    return {"status": "ok", "message": "API está funcionando corretamente."}

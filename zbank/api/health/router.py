from fastapi import APIRouter


health_router = APIRouter(prefix="/health", tags=["health"])


@health_router.get(
    "/",
    description="Проверяет работспособность API",
    response_description="Строка, представляющая состояние сервиса",
)
async def health():
    return {"detal": "alright."}

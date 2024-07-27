from fastapi import APIRouter


router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "/",
    description="Проверяет работспособность API",
    response_description="Строка, представляющая состояние сервиса",
)
async def health():
    return {"detal": "alright."}

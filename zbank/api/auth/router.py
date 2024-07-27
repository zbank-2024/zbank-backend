from typing import Annotated

from fastapi import APIRouter, Depends, status

from zbank.api.auth.schemas import TokenResponse
from zbank.api.auth.services import authentication, refresh_session


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post(
    "/token/",
    status_code=status.HTTP_201_CREATED,
    description="Аутентификация пользователя",
    response_description="Пара токенов для авторизации.",
)
async def authenticate_user(
    tokens: Annotated[TokenResponse, Depends(authentication)],
):
    return tokens


@router.post(
    "/refresh/",
    description="Обновление токена доступа.",
    response_description="Пара обновленных токенов для авторизации.",
)
async def refresh_token(
    tokens: Annotated[TokenResponse, Depends(refresh_session)],
):
    return tokens

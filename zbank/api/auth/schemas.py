from pydantic import BaseModel, Field


class AuthBaseSchema(BaseModel):
    username: str = Field(
        description="Логин пользователя.",
    )
    password: str = Field(
        description="Пароль пользователя.",
    )


class TokenResponse(BaseModel):
    access_token: str = Field(
        description="Токен доступа.",
    )
    refresh_token: str = Field(
        description="Токен обновления токена доступа.",
    )
    token_type: str = Field(
        default="Bearer",
        description="Тип токена доступа.",
    )


class TokenData(BaseModel):
    sub: str = Field(
        description="Логин пользователя.",
    )
    exp: int = Field(
        description="UNIX время активности токена.",
    )


class RefreshTokenRequest(BaseModel):
    access_token: str = Field(
        description="Старый токен доступа.",
    )

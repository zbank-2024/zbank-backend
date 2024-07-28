from datetime import datetime, timedelta
from typing import Literal

import jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from zbank.api.auth.exceptions import credentials_exception
from zbank.api.auth.schemas import TokenData, TokenResponse
from zbank.config.main import settings
from zbank.models.users import Users


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

token_expires_mapping = {
    "access": settings.JWT_ACCESS_TOKEN_EXPIRES,
    "refresh": settings.JWT_REFRESH_TOKEN_EXPIRES,
}
token_secret_mapping = {
    "access": settings.JWT_ACCESS_TOKEN_SECRET,
    "refresh": settings.JWT_REFRESH_TOKEN_SECRET,
}


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def parse_token(
    token: str,
    token_type: Literal["access", "refresh"],
):
    if token_type not in ("access", "refresh"):
        raise ValueError("token_type must be 'access' or 'refresh'")
    try:
        payload = jwt.decode(
            token,
            token_secret_mapping[token_type],
            algorithms=[settings.JWT_ALGORITHM],
        )
    except jwt.InvalidTokenError:
        raise credentials_exception

    username: str = payload.get("sub")
    if not username:
        raise credentials_exception
    return username


async def create_token(
    data: dict,
    token_type: Literal["access", "refresh"],
):
    if token_type not in ("access", "refresh"):
        raise ValueError("token_type must be 'access' or 'refresh'")

    expires = datetime.now() + timedelta(
        minutes=token_expires_mapping[token_type],
    )
    return jwt.encode(
        TokenData(
            **data,
            exp=int(expires.timestamp()),
        ).model_dump(exclude_defaults=True),
        token_secret_mapping[token_type],
        algorithm=settings.JWT_ALGORITHM,
    )


async def get_user_by_username(
    username: str,
    session: AsyncSession,
):
    user = await session.scalar(
        select(Users).filter_by(username=username),
    )
    if not user:
        raise credentials_exception

    return user


async def generate_token_pair(
    user: Users,
):
    access_token = await create_token(
        dict(sub=user.username),
        token_type="access",
    )
    refresh_token = await create_token(
        dict(sub=user.username),
        token_type="refresh",
    )
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )

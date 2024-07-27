from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from zbank.api.auth.exceptions import credentials_exception
from zbank.api.auth.schemas import RefreshTokenRequest
from zbank.api.auth.utils import (
    generate_token_pair,
    get_user_by_username,
    parse_token,
)
from zbank.database import SessionDep
from zbank.models.users import Users


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/token/")


async def authentication(
    data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep,
):
    user_result = await session.execute(
        select(Users).filter_by(
            username=data.username,
            password=data.password,
        ),
    )

    try:
        user = user_result.scalar_one()
    except NoResultFound:
        raise credentials_exception

    return await generate_token_pair(user)


async def refresh_session(
    data: RefreshTokenRequest,
    session: SessionDep,
):
    username = await parse_token(data.access_token, token_type="access")
    if not username:
        raise credentials_exception

    user = await get_user_by_username(username, session)
    return await generate_token_pair(user)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: SessionDep,
):
    username = await parse_token(token, token_type="access")
    return await get_user_by_username(username, session)

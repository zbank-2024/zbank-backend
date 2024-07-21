from collections.abc import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncAttrs,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from .config.main import settings


engine = create_async_engine(settings.database_dsn, echo=True)
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase, AsyncAttrs):
    metadata = MetaData()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as exc:
            await session.rollback()
            raise exc
        else:
            await session.commit()

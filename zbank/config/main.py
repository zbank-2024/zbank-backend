from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_DSN: PostgresDsn

    @property
    def database_dsn(self) -> str:
        return self.DATABASE_DSN.unicode_string()


settings = Settings()

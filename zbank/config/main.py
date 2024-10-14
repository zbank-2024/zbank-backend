from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_DSN: PostgresDsn
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: int = 12345
    DATABASE_NAME: str = "zbank"
    DATABASE_PORT: int = 5432

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_SECRET: str
    JWT_REFRESH_TOKEN_SECRET: str
    JWT_ACCESS_TOKEN_EXPIRES: int
    JWT_REFRESH_TOKEN_EXPIRES: int

    @property
    def database_dsn(self) -> str:
        return self.DATABASE_DSN.unicode_string()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

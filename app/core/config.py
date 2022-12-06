import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str

    SERVER_HOST: str
    SERVER_PORT: int
    SERVER_CONTEXT_PATH: str

    DATABASE_URL: str
    DATABASE_ECHO: bool

    SUPERUSER_USERNAME: str
    SUPERUSER_PASSWORD: str

    TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    TOKEN_SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

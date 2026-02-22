from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    AUTH_SERVICE_URL: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        case_sensitive = True

settings = Settings()

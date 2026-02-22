from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    PASSWORD_HASHING_ALGORITHM: str

    class Config:
        env_file = "./auth_service/.env"

settings = Settings()

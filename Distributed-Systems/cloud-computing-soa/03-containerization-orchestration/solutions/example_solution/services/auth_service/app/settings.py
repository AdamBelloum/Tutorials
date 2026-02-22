from pydantic_settings import BaseSettings
from pydantic import root_validator
from typing import Dict


class Settings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    PASSWORD_HASHING_ALGORITHM: str
    JWT_HEADER_ALG: str
    JWT_HEADER_TYP: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    REDIS_HOST: str
    REDIS_PORT: int

    JWT_HEADER: Dict[str, str] = {}

    @root_validator(pre=True)
    def create_jwt_header(cls, values) -> Dict: # pylint: disable=no-self-argument
        values['JWT_HEADER'] = {
            'alg': values.get('JWT_HEADER_ALG', ''),
            'typ': values.get('JWT_HEADER_TYP', ''),
        }
        return values

    class Config:
        case_sensitive = True

settings = Settings()

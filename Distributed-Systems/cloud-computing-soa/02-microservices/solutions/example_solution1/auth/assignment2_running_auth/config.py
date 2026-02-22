from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "local"
    secret_key: str = "my_secret_key"

    # Read settings from .env file
    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings from: {settings.env_name}")
    return settings
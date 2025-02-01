import os 
import sys

from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    access_token_expire_minutes: int = 30
    environment: str = "dev"
    secret_key: str = "./src"
    db_password: str
    pythonpath: str
    algorithm: str = "HS256"
    db_user: str
    db_host: str
    db_port: str
    db_name: str
    db_uri: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()

# # print(f"Loaded settings: {settings.dict()}")
# if settings.pythonpath not in sys.path:
#     sys.path.append(os.path.abspath(settings.pythonpath))
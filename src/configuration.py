from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str
    pythonpath: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    db_uri: str
 
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
#print(f"Loaded settings: {settings.dict()}")
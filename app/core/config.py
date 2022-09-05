from pydantic import BaseSettings

class Settings(BaseSettings):
    SERVER_HOST: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
    
settings = Settings()
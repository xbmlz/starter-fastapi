from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str

    class Config:
        case_sensitive = True
    
settings = Settings()
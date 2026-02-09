from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/cattle_db"
    AWS_ACCESS_KEY: str = ""
    AWS_SECRET_KEY: str = ""
    S3_BUCKET: str = "cattle-photos"
    S3_REGION: str = "us-east-1"
    SECRET_KEY: str = "your-super-secret-key-change-in-production"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
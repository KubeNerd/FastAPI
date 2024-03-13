from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
import os

class Settings(BaseSettings):
    API_V1_STR: str = os.getenv('API_V1_STR')
    DB_URL: str = os.getenv('JWT_SECRET')
    BDBaseModel = declarative_base()
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    ALGORITHN: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 20 * 7
    class Config:
        case_sensitive = True
'''
    import secrets
    token: str = secrets.token_urlsafe(32)
'''
settings: Settings = Settings()
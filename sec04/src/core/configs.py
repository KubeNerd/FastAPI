from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"                                                     # Rota da API
    PROJECT_NAME: str = "FastAPI"                                                   # Nome do projeto
    DB_URL: str = "postgresql+asyncpg://fastidb:admindb@localhost:5234/faculdade"
    DBBaseModel: declarative_base() = declarative_base()                          # Modelo base do banco de dados

    class Config:
        case_sensitive = True                                                       # Configurações sensíveis ao caso

settings = Settings()                                                              # Instância das configurações
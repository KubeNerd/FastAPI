from prisma import Prisma
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    PRISMA_CLIENT: Prisma = Prisma()


settings: Settings = Settings()
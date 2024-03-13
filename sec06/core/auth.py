from pytz import timezone
from typing import Optional, List
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.usuario_model import UsuarioModel
from core.config import settings
from core.security import verificar_senha

from pydantic import EmailStr


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/usuarios/login'
)


async def authentiar(email: str, senha: str, db:AsyncSession) -> Optional[UsuarioModel]:
    pass
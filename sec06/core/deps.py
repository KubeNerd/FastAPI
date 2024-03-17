from typing import Generator, Optional
from fastapi import Depends, HTTPException, status

from jose import jwt, JOSEError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel


from core.database import Session
from core.auth import oauth2_schema
from core.config import settings
from models.usuario_model import UsuarioModel


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()

async def get_current_user(db: Session = Depends(get_session), token: str = Depends(oauth2_schema)) -> UsuarioModel:
    credential_excepetion: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Nã foi possivel autenticiar  a credencial informada',
        headers={'www-Authenticate':'Bearer'}
        )
    
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHN],
            options={'verify_aud': False }            
        )

        username: str = payload.get('sub')

        if username is None:
            raise credential_excepetion
        
        token_data: TokenData = TokenData(username=username)

    except JOSEError:
        raise credential_excepetion
    
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username))
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if usuario is None:
            raise credential_excepetion

    return usuario
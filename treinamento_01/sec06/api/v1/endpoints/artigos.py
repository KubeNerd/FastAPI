from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.artigo_model import ArtigoModel
from models.usuario_model import UsuarioModel
from schemas.artigos_schema import ArtigoSchema
from core.deps import get_session, get_current_user


router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ArtigoModel)
async def post_artigo(
    artigo: ArtigoSchema,
    usuario_logado: UsuarioModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session) 
):
    novo_artigo: ArtigoModel = ArtigoModel(
        titulo=artigo.titulo,
        descricao=artigo.descricao,
        url_fonte=artigo.url_fonte,
        usuario_id=usuario_logado.id
    )

    db.add(novo_artigo)
    await db.commit()

    return novo_artigo
from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Response, Request, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_model import CursoModel
from core.deps import get_session

# Bypass warning SQLMOdel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True # type: ignore
Select.inherit_cache = True

# Fim Bypass
router = APIRouter()

# POST Curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_cursos(curso=CursoModel, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)
    await db.commit()
    return novo_curso

# Get Cursos
@router.get('/', status_code=status.HTTP_200_OK,  response_model=List[CursoModel])
async def get_cursos(db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()

        return cursos
    
# Get Curso
@router.get('/{curso_id}', response_model=CursoModel, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado.', status_code=status.HTTP_404_NOT_FOUND)
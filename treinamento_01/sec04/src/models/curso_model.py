from core.configs import settings

from sqlalchemy import Column, Integer, String

class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)  # ID DO CURSO
    titulo: str = Column(String(100), nullable=False, unique=True)   # TÍTULO DO CURSO - NÃO PODE SER NULO E NÃO PODE TER DUPLICIDADE
    aulas: int = Column(Integer, nullable=False)                     # QUANTIDADE DE AULAS - NÃO PODE SER NULO
    horas: int = Column(Integer, nullable=False)       
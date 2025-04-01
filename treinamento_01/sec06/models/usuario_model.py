from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from core.config import settings

class UsuarioModel(settings.BDBaseModel):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, unique=True)
    senha = Column(String(256), nullable=False),
    eh_admin = Column(Boolean, default=False),
    artigos = relationship(
        'ArtigosModel',
        cascade='all, delete-orphan',
        back_populates='criador',
        userlist=True,
        lazy='joined'
    )
from typing import Optional, List
from pydantic import EmailStr ,BaseModel as ScBaseModel
from schemas.artigos_schema import ArtigoSchema

class UsuariosSchemaBase(ScBaseModel):
    id: Optional[int]
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False


    class Config:
        orm_mode: True


class UsuarioSchemaCreate(UsuariosSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuariosSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuariosSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin:Optional[bool]

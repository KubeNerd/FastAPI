from typing import Optional
from pydantic import HttpUrl, BaseModel as ScBaseModel

class ArtigoSchema(ScBaseModel):
    id: Optional[int] = None
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    class Config:
        orm_mode = True


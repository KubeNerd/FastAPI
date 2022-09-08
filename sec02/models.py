from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(" ")
        if len(palavras) < 3:
            raise ValueError("O titulo deve ter pelo menos 3 palavras.")

        if value.islower():
            return ValueError("O titulo deve ser capitalizado.")
        return value

    @validator("aulas")
    def validar_horas(cls, value:int):
        if value > 12:
            raise ValueError("O titulo deve ter pelo menos 3 palavras.")



cursos = [
    Curso(id=1, titulo="Programaçao para leigos", aulas=42, horas=56),
    Curso(id=2, titulo="Algoritimos de Programação", aulas=52, horas=300)
]
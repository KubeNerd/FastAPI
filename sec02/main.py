from typing import Any
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi import status
from models import Curso
from fastapi import Query
from fastapi import Path
from fastapi import Header
from time import sleep
from fastapi import Depends



app = FastAPI(title="API do Vinicius", version="0.0.1")

cursos = {1: {"titulo": "Programação para leitos", "aulas": 112, "horas": 58}, 2: {
    "titulo": "Algoritimos e logica de programação", "aulas": 87, "horas": 67}, 3:{
        "titulo": "Orientação a Objetos", "aulas": 50, "horas": 12
    }}

def fake_db():
    try:
        print("Abrindo conexão com o banco de dados...")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados ...")
        sleep(1)




@app.get("/dep_cursos")
async def dep_cursos(db:Any = Depends(fake_db)):
    return cursos

@app.get("/cursos", response_model=Curso)
async def get_cursos(db:Any = Depends(fake_db)):
    return cursos



@app.get('/cursos/{curso_id}')
async def get_curso_by_id(curso_id: int, db:Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except TypeError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="ID passado como parametro bugado!")


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Já existe um {curso.id}')


@app.put('/cursos{curso_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um curso com o id {curso_id}'
        )

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
  if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
  else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um curso com o id {curso_id}')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1",
                port=3000, debug=True, reload=True)
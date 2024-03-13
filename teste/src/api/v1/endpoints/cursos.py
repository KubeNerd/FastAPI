from fastapi import APIRouter, status


router = APIRouter()

cursos = {1: {"titulo": "Programação para leitos", "aulas": 112, "horas": 58}, 2: {
    "titulo": "Algoritimos e logica de programação", "aulas": 87, "horas": 67}, 3:{
        "titulo": "Orientação a Objetos", "aulas": 50, "horas": 12
    }}


@router.get('/', status_code=status.HTTP_200_OK)
def get_cursos():
    return cursos

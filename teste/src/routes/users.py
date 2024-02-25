from fastapi import APIRouter

users_route = APIRouter()

cursos = {1: {"titulo": "Programação para leitos", "aulas": 112, "horas": 58}, 2: {
    "titulo": "Algoritimos e logica de programação", "aulas": 87, "horas": 67}, 3:{
        "titulo": "Orientação a Objetos", "aulas": 50, "horas": 12
    }}


@users_route.get('/users')

async def main():
    return cursos

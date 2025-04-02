#  Diferença entre síncrono e assíncrono
import time
def read_data():
    time.sleep(2)
    return "dados"
 # - Isso bloqueia por 2 segundos. Nada mais roda nesse tempo. 


# async e await são usados para programação assíncrona:

'''
    Eles permitem que você escreva código que parece síncrono, mas que não bloqueia a thread principal — ideal pra operações de I/O (esperar resposta de rede, banco, arquivos).

'''

'''import asyncio


async def sum(a, b):
    return a + b

async def print_sum(a, b):
    result = await sum(a, b)
    print(f'resultado igual a {result}')

'''



'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}


'''


import asyncio

async def read_data():
    await asyncio.sleep(2)
    return "dados"

 # Aqui o await asyncio.sleep(2) não bloqueia o loop principal. Enquanto espera, o interpretador pode rodar outras funções async.


# Estrutura de uso
# Definir uma função como assíncrona com async def
# Chamar funções assíncronas usando await

'''
   Artigo sobre PrismaORM https://medium.com/dooboolab/prisma-with-python-and-fastapi-33bf25bb20c0
'''

from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app: FastAPI = FastAPI(title='FastAPI'
                       )
@app.get('/')
async def get_routes():
    return {}

app.include_router(api_router, prefix=settings.API_V1_STR)


# uvicorn main:app --port 3333 --host '127.0.0.1

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8089, log_level='info', reload=True)

    
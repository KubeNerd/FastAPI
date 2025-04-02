from fastapi import FastAPI
import uvicorn
from routers.api import api_router

app = FastAPI(title="Primeira API do Treinamento")

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)
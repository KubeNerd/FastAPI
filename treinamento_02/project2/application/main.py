from fastapi import FastAPI
import uvicorn
from routes.health_check import health_check_router

app = FastAPI(title="SEGUNDO PROJETO - API")
app.include_router(health_check_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=8080)
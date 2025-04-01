from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/api")
async def read_root():
    return {"Hello":"World"}


@app.post("/api/users")

async def users():
    return {"users":{}}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info", reload=True)
from fastapi import FastAPI
from routes import routes
import sqlite3

app = FastAPI()

app.include_router(routes.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, debug=True)
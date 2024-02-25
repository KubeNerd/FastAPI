from fastapi import FastAPI
from src.routes.healthcheck import healthcheck
from src.routes.sendmessages import messages
from src.routes.users import users_route

app = FastAPI(version='0.0.1.2', summary='My Teste API With FastAPI')

app.include_router(healthcheck)
app.include_router(messages)
app.include_router(users_route)
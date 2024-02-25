from fastapi import APIRouter, status

messages = APIRouter()

@messages.post('/sendmessages', status_code=status.HTTP_201_CREATED)
async def main():
    return {}

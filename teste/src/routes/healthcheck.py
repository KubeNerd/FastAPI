from fastapi import APIRouter, HTTPException, status

healthcheck = APIRouter()

@healthcheck.get('/healthcheck')

async def main():
    try:
        return { "status":"ok" } 
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT)
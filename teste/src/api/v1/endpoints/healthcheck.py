from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get('/')

def get_healthcheck():
    try:
        return { "status":"ok" } 
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT)
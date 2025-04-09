from fastapi import FastAPI
from http import HTTPStatus
from schemas import Message, UserSchema, UserPublic, UserDB
import uvicorn

app = FastAPI()


database = []

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def message():
    return {"message": {
        "status": 200
    }}

@app.post("/create/user", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )


    database.append(user_with_id)
    
    return user_with_id


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, log_level="info")

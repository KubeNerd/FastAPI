# Daddos de usuário

# name: string
# age: integer
# email: string


from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid e-mail")
        return value

# user = User(name="Vinicius", age=55, email="vinicius551@contato.com")

def f(user: User):
    if "vinicius55@contato.com" in user.email:
        pass
    else:
        return user.email
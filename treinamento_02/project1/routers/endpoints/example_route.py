from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field

exemple_router: APIRouter = APIRouter()


# ===============================
# 📡 ROTA: GET /
# ===============================
@exemple_router.get("/", tags=["Healthcheck"], summary="Verifica se o serviço está online")
def read_root():
    """
    Rota de verificação de disponibilidade da API.

    Retorna uma mensagem padrão em JSON indicando que a API está funcional.
    """
    return {"status": "poing"}


# ===============================
# 🔢 ROTA: GET /items/{item_id}
# Path + Query parameters
# ===============================
@exemple_router.get("/items/{item_id}", tags=["Exemplos"], summary="Retorna item com base em parâmetros de rota e query")
def read_item(
    item_id: int = Path(..., title="ID do item", ge=1),
    q: str = Query(None, max_length=50, description="Texto de busca opcional")
):
    """
    Retorna informações do item com base no ID (path) e parâmetro de busca (query).
    - `item_id` é obrigatório e deve ser um número inteiro >= 1.
    - `q` é opcional e representa um filtro de busca.
    """
    return {"item_id": item_id, "query": q}


# ===============================
# 🧾 Modelo para Body parameter
# ===============================
class User(BaseModel):
    name: str = Field(..., example="João da Silva")
    email: str = Field(..., example="joao@email.com")
    age: int = Field(..., gt=0, example=30)


# ===============================
# 🧍 ROTA: POST /users
# Body parameter com validação
# ===============================
@exemple_router.post("/users", tags=["Exemplos"], summary="Cria um novo usuário com dados enviados no corpo")
def create_user(user: User = Body(..., description="Dados do usuário no corpo da requisição")):
    """
    Cria um novo usuário com base nos dados enviados no corpo da requisição.

    - Campos obrigatórios: `name`, `email`, `age`
    - Validações:
        - `age` deve ser > 0
        - `email` deve ser string (validação extra pode ser adicionada)
    """
    return {"message": "Usuário criado com sucesso", "user": user}

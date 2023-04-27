from fastapi import FastAPI
from pydantic import BaseModel

router = FastAPI()


class User(BaseModel):  # BaseModel da la capacidad de crear una entidad
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="pepito", surname="Sanchez", url = "https://pepito.dev", age = 20),
              User(id=2, name = "Pancracio", surname = "David", url =  "https://pancracio.com", age = 55),
              User(id=3, name="Pepita", surname="Maria", url="https://pepita.com", age=33)]


@router.get("/usersjson")
async def users_json():  # Creamos un JSON a mano
    return [{"name": "Pepito", "surname": "Sanchez", "url": "https://pepito.dev", "age": 20},
            {"name": "Pancracio", "surname": "David", "url": "https://pancracio.com", "age": 55},
            {"name": "Pepita", "surname": "Maria", "url": "https://pepita.com", "age": 33}]


@router.get("/user")
async def users():
    return users_list


@router.get("/user/{id}")  # Path
async def user(id: int):
    """
    http://127.0.0.1:8000/users/1....2.....4
    Args:
        id: int -> identificador de la lista de usuarios

    Returns:
        la lista de usuarios que sean identificados con ese "id"
    """
    return search_user(id)


def search_user(id: int):
    """
    Guardar en una lista los usuarios cuyo parámetro id sea el mismo que el "id" del usuario
    Args:
        id:

    Returns:
        lista de usuarios
        error en caso de sobrepasar el "id" de la lista
    """
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

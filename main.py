from fastapi import FastAPI
from models import User

app = FastAPI()

# Lista para almacenar usuarios
users = []

@app.post("/add_user/", response_model=User)  # Utilizando User como modelo de respuesta
async def add_user(user: User):
    users.append(user)
    return user  # Ahora devolvemos el objeto User

@app.get("/get_user/{user_name}", response_model=User)  # Utilizando User como modelo de respuesta
async def get_user(user_name: str):
    for user in users:
        if user.name == user_name:
            return user
    return {"message": "User not found"}

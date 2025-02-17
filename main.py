from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

users = []

@app.post("/add_user/")
async def add_user(user: User):
    users.append(user)
    return {"message": "User added successfully"}

@app.get("/get_user/{user_name}")
async def get_user(user_name: str):
    for user in users:
        if user.name == user_name:
            return user
    return {"message": "User not found"}

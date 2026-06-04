from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

user_db: Dict[str, str] = {}

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User):
    if user.username in user_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    user_db[user.username] = user.password
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: User):
    if user.username not in user_db or user_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "username": user.username}

@app.get("/dashboard/{username}")
async def dashboard(username: str):
    if username not in user_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Welcome to your dashboard, {username}!"}

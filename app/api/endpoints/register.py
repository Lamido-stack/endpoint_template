from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserRegistration(BaseModel):
    username: str
    password: str
    email: str

@router.post("/register")
async def register(user: UserRegistration):

    return {"message": "User registered successfully", "user": user.username}
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def sign_in_user(username: str, password: str):
    
    return {"message": "User signed in successfully", "username": username}
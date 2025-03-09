from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.v1.models.user_model import User
from app.api.v1.services.crud import create_user
from app.database import get_db
from app.api.v1.schemas.user_schema import UserCreate
from app.api.v1.utils.auth import hash_password
from app.api.v1.services.crud import get_user_by_username

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):

    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exist")
    
    hashed_password = hash_password(user.password)
    
    new_user = create_user(db=db, username=user.username, password_hash=hashed_password)
    
    return {"message": "User created successfully", "username": new_user.username}

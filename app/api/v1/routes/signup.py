from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.v1.models.user_model import User
from app.api.v1.services.crud import create_user
from app.database import get_db
from app.api.v1.schemas.user_schema import UserCreate
from app.api.v1.utils.auth import hash_password

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exist")
    
    hashed_password = hash_password(user.password)
    
    new_user = create_user(db=db, username=user.username, password_hash=hashed_password)
    
    return {"message": "User created successfully", "username": new_user.username}

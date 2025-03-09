from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from app.api.v1.models.user_model import User
from app.api.v1.schemas.user_schema import UserCreate
from app.api.v1.utils.auth import hash_password
router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}

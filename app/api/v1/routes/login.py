from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.v1.models.user_model import User
from app.api.v1.utils.auth import verify_password
from app.database import get_db
from app.api.v1.schemas.user_schema import UserCreate
from app.api.v1.services.crud import get_user_by_username

router = APIRouter()


@router.post("/login")
async def login(user: UserCreate, db: Session = Depends(get_db)):
    
    db_user = get_user_by_username(db, user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    return {"message": "Login successful"}

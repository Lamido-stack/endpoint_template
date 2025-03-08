from sqlalchemy.orm import Session
from app.api.v1.models.user_model import User

def create_user(db: Session, username: str, password_hash: str):
    db_user = User(username=username, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

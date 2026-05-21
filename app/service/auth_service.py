from sqlalchemy.orm import Session 
from app.models.user import User
from app.schema.auth import UserRegister, UserLogin

from app.core.security import hash_password, verify_password, create_access_token

def register_user(
        db: Session,
        user: UserRegister
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()
    if existing_user:
        return None
    db_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(
        db: Session,
        email: str,
        password: str
):
    user = db.query(User).filter(
        User.email == email
    ).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    
    access_token = create_access_token({
        "sub": user.email
    })
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
from sqlalchemy import select
from app.models import User
from passlib.hash import bcrypt
from fastapi import HTTPException

async def get_user_by_email(session, email):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()

async def create_user(session, email, password):
    user = await get_user_by_email(session, email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(email=email, password_hash=bcrypt.hash(password))
    session.add(new_user)
    await session.commit()
    return new_user

async def authenticate_user(session, email, password):
    user = await get_user_by_email(session, email)
    if not user or not bcrypt.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

from fastapi import APIRouter, Depends
from app.schemas import RegisterModel, LoginModel
from app.crud import create_user, authenticate_user
from app.deps import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/register")
async def register(data: RegisterModel, session: AsyncSession = Depends(get_session)):
    await create_user(session, data.email, data.password)
    return {"msg": "Registration successful"}

@router.post("/login")
async def login(data: LoginModel, session: AsyncSession = Depends(get_session)):
    await authenticate_user(session, data.email, data.password)
    return {"msg": "Login successful"}

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from services.auth_service import signup, signin
from models.user_model import UserCreate, UserInDB
from db import get_database

router = APIRouter()

@router.post("/signup")
async def register_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await signup(user, db)

@router.post("/signin")
async def login_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await signin(user, db)

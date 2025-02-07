from ..models.user import User, UserInDB
from ..db import db
from ..utils import get_hashed_password, verify_password, create_access_token
from fastapi import HTTPException, status

async def create_user(user: User):
    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = get_hashed_password(user.password)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    await db["users"].insert_one(user_in_db.dict())
    return {"message": "User created successfully"}

async def authenticate_user(email: str, password: str):
    user = await db["users"].find_one({"email": email})
    if user and verify_password(password, user["hashed_password"]):
        token = create_access_token({"sub": user["email"]})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )
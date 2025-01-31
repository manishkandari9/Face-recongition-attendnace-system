from fastapi import APIRouter, HTTPException, Depends
from models.user_model import User, UserInDB
from services.auth_service import hash_password, verify_password, create_jwt_token
from database import users_collection

auth_router = APIRouter()

@auth_router.post("/signup")
async def signup(user: User):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)
    user_data = {"email": user.email, "roll_number": user.roll_number, "hashed_password": hashed_password}
    await users_collection.insert_one(user_data)

    return {"message": "User created successfully"}

@auth_router.post("/signin")
async def signin(user: User):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token({"email": user.email})
    return {"token": token}

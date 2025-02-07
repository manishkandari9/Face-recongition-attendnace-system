from fastapi import APIRouter, Depends
from ..models.user import User
from ..controllers import auth_controller
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/signup", response_description="Sign up new user")
async def signup(user: User):
    return await auth_controller.create_user(user)

@router.post("/signin", response_description="Sign in user")
async def signin(user: User):
    token = await auth_controller.authenticate_user(user.email, user.password)
    return JSONResponse(content=token)
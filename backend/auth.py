from fastapi import APIRouter, HTTPException
from app import crud
from app.schemas import UserCreateSchema, UserResponseSchema
from app.utils import verify_password

router = APIRouter()

# Route to sign up
@router.post("/api/auth/signup", response_model=UserResponseSchema)
async def signup(user: UserCreateSchema):
    # Check if the identifier exists
    existing_user = await crud.get_user_by_identifier(user.identifier)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Create new user
    new_user = await crud.create_user(user)
    return new_user

# Route to sign in
@router.post("/api/auth/signin")
async def signin(user: UserCreateSchema):
    # Find user by identifier
    db_user = await crud.get_user_by_identifier(user.identifier)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": db_user}

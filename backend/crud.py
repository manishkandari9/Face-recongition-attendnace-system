from app.models import UserCreate, UserInDB
from app.database import db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Helper to hash password
def get_password_hash(password: str):
    return pwd_context.hash(password)

# CRUD operation for creating a new user
async def create_user(user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    new_user = await db.users.insert_one(user_dict)
    return {**user.dict(), "id": str(new_user.inserted_id)}

# CRUD operation for fetching user by identifier
async def get_user_by_identifier(identifier: str) -> UserInDB:
    user = await db.users.find_one({"identifier": identifier})
    if user:
        return UserInDB(**user)
    return None

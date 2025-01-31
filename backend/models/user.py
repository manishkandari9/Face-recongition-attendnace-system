from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    roll_number: Optional[str] = None
    password: str  # Plain password (will be hashed before saving)

class UserInDB(User):
    hashed_password: str  # This will store hashed password

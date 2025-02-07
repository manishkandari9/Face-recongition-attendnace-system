from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    roll_number: Optional[str]
    password: str

class UserInDB(User):
    hashed_password: str

class UserInResponse(BaseModel):
    email: EmailStr
    roll_number: Optional[str]
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    identifier: str  # Can be email or roll number
    password: str

class UserCreate(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

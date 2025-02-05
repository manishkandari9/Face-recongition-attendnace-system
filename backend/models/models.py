from pydantic import BaseModel, EmailStr, constr, validator
from bson import ObjectId
import re

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# Base User model for common fields
class UserBase(BaseModel):
    identifier: str
    password: str

    class Config:
        orm_mode = True

    @validator("identifier")
    def validate_identifier(cls, v):
        if not re.match(r"^[a-zA-Z0-9]+(?:[._-]?[a-zA-Z0-9]+)*@[a-zAZ0-9-]+\.[a-zA-Z0-9-.]+$", v):
            if not re.match(r"^[0-9]{6,12}$", v):
                raise ValueError("Identifier should be a valid email or roll number (6 to 12 digits)")
        return v

class UserCreate(UserBase):
    pass

class UserInDB(UserBase):
    id: PyObjectId

    class Config:
        json_encoders = {
            ObjectId: str
        }

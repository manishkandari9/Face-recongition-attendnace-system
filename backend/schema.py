from pydantic import BaseModel

class UserBaseSchema(BaseModel):
    identifier: str
    password: str

class UserCreateSchema(UserBaseSchema):
    pass

class UserResponseSchema(UserBaseSchema):
    id: str

    class Config:
        orm_mode = True

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str
    old_password: str
    new_password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreateResponse(BaseModel):
    id: int
    username: str

class UserValidateResponse(BaseModel):
    id: int
    username: str
# pydiantic user model 

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class UserNewPassword(User):
    new_password: str

class Token(BaseModel):
    token: str
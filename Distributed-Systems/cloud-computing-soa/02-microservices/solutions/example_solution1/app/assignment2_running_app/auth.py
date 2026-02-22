import jwt
from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import requests

app = FastAPI()


# In-memory database
users_db = {}


class User(BaseModel):
    username: str
    password: str


class UpdatePassword(BaseModel):
    username: str
    password: str
    new_password: str


class Login(BaseModel):
    username: str
    password: str


@app.post('/users', status_code=201)
def create_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=409, detail="Username already exists")

    users_db[user.username] = user.password
    return {"msg": "User created"}


@app.put('/users')
def update_password(update_info: UpdatePassword):
    username = update_info.username
    old_password = update_info.password
    new_password = update_info.new_password

    if username not in users_db or old_password!=users_db[username]:
        raise HTTPException(status_code=403, detail="Forbidden")

    users_db[username] = new_password
    return {"msg": "Password updated"}

def generate_token(username):
    payload = {
        "username": username,
    }

    token = jwt.encode(payload, "key", algorithm="HS256")

    return token
@app.post('/users/login')
def login(login_info: Login):
    username = login_info.username
    password = login_info.password

    if username not in users_db or password!=users_db[username]:
        raise HTTPException(status_code=403, detail="Forbidden")
    access_token = generate_token(username)
    response = requests.post(
        "http://localhost:8000/login",
        json={"username": username, "Authorization": access_token},
    )
    return {"token": access_token}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

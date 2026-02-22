from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, Request
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt
from passlib.context import CryptContext

from app.constants.const import PASSWORD_HASHING_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from app.utils.db import get_db
from app.schemas.token import TokenPayload

def reusable_oauth2(request: Request):
    token = request.headers.get("Authorization")
    if token:
        token = token.split("Bearer ")[-1]
    return token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Security:
    @staticmethod
    async def hash_password(password):
        return pwd_context.hash(password) # hash password

    @staticmethod
    async def create_access_token(subject):
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES # default: 8 days
        )
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=PASSWORD_HASHING_ALGORITHM) # encode JWT token
        return encoded_jwt

    @staticmethod
    async def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    async def get_current_user(token: str = Depends(reusable_oauth2), db: AsyncSession = Depends(get_db)):
        if not token:
            return None
        try:
            payload = jwt.decode(
                token, SECRET_KEY, algorithms=[PASSWORD_HASHING_ALGORITHM] # decode token to get user_id
            )
            token_data = TokenPayload(**payload)
        except (jwt.JWTError, ValidationError):
            raise HTTPException(status_code="403", detail="Could not validate credentials")

        from app.services.user_service import get_user_by_id
        user = await get_user_by_id(db, id=token_data.sub) # check user_id existing in database
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user.id
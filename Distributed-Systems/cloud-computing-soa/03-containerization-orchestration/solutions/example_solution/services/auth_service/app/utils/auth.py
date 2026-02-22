from app.utils.jwt import JWT
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Auth:
    @staticmethod
    async def create_access_token(user):
        try:
            encoded_jwt = JWT.encode(user=user)
            return encoded_jwt
        except Exception as e:
            print("Error - auth: create access token", e)
            return None
        
    
    
    @staticmethod
    async def hash_password(password):
        return pwd_context.hash(password) # hash password
    
    @staticmethod
    async def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

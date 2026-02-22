from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    token: str

class TokenPayload(BaseModel):
    user: Optional[int] = None
    exp: Optional[int] = None
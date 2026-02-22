from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.utils.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    urls = relationship("URL", back_populates="owner") # user can have many urls
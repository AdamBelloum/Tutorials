from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.utils.db import Base

class URL(Base):
    __tablename__ = 'urls'

    id = Column(String, primary_key=True, index=True)
    value = Column(String, index=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    owner = relationship("User", back_populates="urls") # url can have one user
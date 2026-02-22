from sqlalchemy import Column, String, Integer

from app.utils.db import Base

class URL(Base):
    __tablename__ = 'urls'

    id = Column(String, primary_key=True, index=True)
    value = Column(String, index=True)
    user_id = Column(Integer, index=True)

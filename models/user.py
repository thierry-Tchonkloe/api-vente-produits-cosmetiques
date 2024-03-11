from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from .base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), unique=False, index=True)
    user_password = Column(String(255))
    user_email = Column(String(255), unique=True, index=True)
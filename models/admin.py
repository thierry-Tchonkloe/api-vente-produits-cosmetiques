from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from .base import Base
from sqlalchemy.orm import relationship


class Admin(Base):
    __tablename__ = 'Admin'
    
    admin_id = Column(Integer, primary_key=True, index=True)
    admin_name = Column(String(50), unique=False, index=True)
    admin_password = Column(String(255))
    admin_email = Column(String(255), unique=True, index=True)
from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, DateTime
from .base import Base


class Command(Base):
    __tablename__ = 'Commands'
    
    command_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50), unique=False, index=True)
    product_nbr = Column(Integer)
    phone_number = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    detail = Column(String(255))
    contact_date = Column(DateTime)
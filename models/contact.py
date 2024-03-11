from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, DateTime
from .base import Base


class Contact(Base):
    __tablename__ = 'contacts'
    
    contact_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), unique=False, index=True)
    last_name = Column(String(50), unique=False, index=True)
    phone_number = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    message = Column(String())
    contact_date = Column(DateTime)
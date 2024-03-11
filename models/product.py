from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Product(Base):
    __tablename__ = 'product'
    
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(250), index=True)
    product_image = Column(String(255), nullable=False, index=True)
    product_prix = Column(String(255), index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

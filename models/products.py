from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Products(Base):
    __tablename__ = 'products'
    
    product_id = Column(String(250), primary_key=True, index=True)
    product_name = Column(String(250), index=True)
    product_nbr = Column(Integer, index=True)
    product_prix = Column(String(255), index=True)
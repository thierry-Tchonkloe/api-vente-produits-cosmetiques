from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from .base import Base
from sqlalchemy.orm import relationship


class Buy(Base):
    __tablename__ = 'Buys'
    
    command_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    status = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    

    
    users = relationship("User", back_populates="Buys")
    product = relationship("Product", back_populates="Buys")
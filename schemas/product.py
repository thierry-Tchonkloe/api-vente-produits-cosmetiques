from pydantic import BaseModel
from typing import List
from datetime import datetime

class ProductBase(BaseModel):
    product_name: str
    product_image: str
    product_prix: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int
    created_at : datetime
    updated_at : datetime

    class Config:
        orm_mode = True
        from_attributes=True
from pydantic import BaseModel
from typing import List

class ProductsBase(BaseModel):
    products_prix: str
    products_name: str
    products_nbr: int

class ProductsCreate(ProductsBase):
    pass

class Products(ProductsBase):
    products_id: int

    class Config:
        orm_mode = True
        from_attributes=True
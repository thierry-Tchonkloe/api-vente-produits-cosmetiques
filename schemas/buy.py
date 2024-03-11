from pydantic import BaseModel
from enum import Enum
from typing import Dict

class StatusEnum(str, Enum):
    Successful= "Successful"
    InProgress = "In Progress"

class BuyBase(BaseModel):
    product_id: int
    user_id: int

class BuyCreate(BuyBase):
    pass

class Buy(BuyBase):
    Buy_id: int
    status: str

    class Config:
        orm_mode = True
        from_attributes=True
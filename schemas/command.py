from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommandBase(BaseModel):
    product_name: str
    product_nbr: str
    email: str
    phone_number: str
    detail: str

class CommandCreate(CommandBase):
    pass

class Command(CommandBase):
    command_id: int
    command_date: datetime

    class Config:
        orm_mode = True
        from_attributes=True
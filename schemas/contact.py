from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    message: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    contact_id: int
    contact_date: datetime

    class Config:
        orm_mode = True
        from_attributes=True
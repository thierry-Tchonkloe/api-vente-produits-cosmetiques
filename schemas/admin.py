from pydantic import BaseModel
from typing import Dict


class AdminBase(BaseModel):
    admin_name: str
    admin_password: str
    admin_email: str
    

class AdminCreate(AdminBase):
    pass

class Admin(AdminBase):
    admin_id: int

    class Config:
        orm_mode = True
        from_attributes=True
        
class LoginDataForm(BaseModel): 
    adminEmail :str
    adminPassword : str
        
class UserLogin(BaseModel): 
    data :  LoginDataForm
from pydantic import BaseModel
from typing import Dict


class UserBase(BaseModel):
    user_name: str
    user_password: str
    user_email: str
    

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
        from_attributes=True
        
class LoginDataForm(BaseModel): 
    user_email :str
    user_password : str
        
class UserLogin(BaseModel): 
    data :  LoginDataForm
    
class PasswordFormat(BaseModel):
    user_id: int
    new_password: str
    old_password: str
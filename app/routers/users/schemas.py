from typing import List, Optional
from pydantic import BaseModel
#from .models import Subject 

class UserBase(BaseModel):
    name: str
    email: str
    first_name: str
    last_name: str
    # image_url: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    active: bool

class User(UserBase):
    id: str
    created_by: int
    account_id: int
    role_id: int
    active: bool
    #teachers: List[Subject] = []

    class Config:
        orm_mode = True


# class SubjectBase(BaseModel):
#     email: str

# class SubjectCreate(SubjectBase):
#     pass

# class Subject(SubjectBase):
#     id: int
#     created_by: int

#     class Config:
#         orm_mode = True

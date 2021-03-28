from typing import List, Optional
from pydantic import BaseModel
#from .models import Subject 

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    name: str
    #is_active: bool
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

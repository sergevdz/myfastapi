from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "sys_users"

    id = Column(Integer, primary_key=True, index=True)
    created_by = Column(Integer, index=True)
    account_id = Column(Integer, index=True)
    role_id = Column(Integer, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    #image_url = Column(String)
    active = Column(Boolean, default=True)

    #subjects = relationship("Subject", back_populates="user_creator")


# class Subject(Base):
#     __tablename__ = "ac_subjects"

#     id = Column(Integer, primary_key=True, index=True)
#     code = Column(String, index=True)
#     name = Column(String, unique=True, index=True)
#     created_by = Column(Integer, ForeignKey("sys_users.id"))

#     user_creator = relationship("User", back_populates="items")

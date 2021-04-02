from sqlalchemy.orm import Session
from pydantic import BaseModel, ValidationError, validator
from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    #return {"userId": user_id}
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    #fake_hashed_password = user.password + "notreallyhashed"
    #db_user = models.User(**user.dict(), created_by=1, account_id=1, role_id=1)
    db_user = models.User(
        created_by=1,
        account_id=1,
        role_id="1",
        name=user.name,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int , user: schemas.UserUpdate):
    # db_user = db.query(models.User).filter(models.User.id == user.id).first()
    db_user = db.query(models.User).get(user_id)
    if (db_user):
        db_user.name = user.name
        db_user.email = user.email
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        # db.update()
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    # db_user = models.User.query.filter(User.id == user_id).delete()
    if (db_user):
        db.delete(db_user)
        db.commit()
    return db_user

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

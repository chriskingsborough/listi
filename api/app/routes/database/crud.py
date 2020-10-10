from sqlalchemy.orm import Session
from . import models, schemas

# Lists
def get_lists(db: Session, offset: int, limit: int):
    return db.query(models.Lists).offset(offset).limit(limit).all()

def get_list(db: Session, id: int):
    return db.query(models.Lists).filter(models.Lists.id == id).first()

def create_list(db: Session, lst: schemas.List):
    db_lst = models.Lists(
        name=lst.name,
        description=lst.description
    )
    db.add(db_lst)
    db.commit()
    db.refresh(db_lst)
    return db_lst

def delete_list(db: Session, id: int):
    lst = db.query(models.Lists).filter(models.Lists.id == id).delete()
    db.commit()
    return

# Items
def get_items(db: Session, id: int):
    items = db.query(models.Items).filter(models.Items.list_id == id).all()
    return items

def delete_item(db: Session, id: int):
    items = db.query(models.Items).filter(models.Items.id == id).delete()
    db.commit()
    return

# Users
def get_user(db: Session, id=None, email=None):
    # use either id or email. email used to verify pw, id for fk requirements
    if id:
        user = db.query(models.User).filter(models.User.id == id).all()
    elif email:
        user = db.query(models.User).filter(models.User.email == email).all()
    else:
        raise ValueError('email or id required')
    return user

def create_user(db: Session, usr: models.User):
    existing = get_user(db, email=usr.email)
    if existing:
        raise ValueError('email already exists.. cannot create new user')
    db_usr = models.User(
        name=usr.name,
        email=usr.email,
        password=usr.password,
        first_name=usr.first_name,
        last_name=usr.last_name,
        date_of_birth=usr.date_of_birth,
        phone_number=usr.phone_number
    )
    db.add(db_usr)
    db.commit()
    db.refresh(db_usr)
    return db_usr


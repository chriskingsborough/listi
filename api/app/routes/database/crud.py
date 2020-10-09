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

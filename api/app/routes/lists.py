from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .database import models, schemas, crud
from .database.database import SessionLocal, engine

router = APIRouter()

# database operations
models.Base.metadata.create_all(bind=engine)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/lists')
def get_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lists = crud.get_lists(db, skip, limit)
    return lists

@router.get('/lists/{list_id}')
def get_list(list_id: int, db: Session = Depends(get_db)):
    lst = crud.get_list(db, list_id)
    return lst

@router.post('/lists')
def post_lists(lst: schemas.List, db: Session = Depends(get_db)):

    db_lst = models.Lists(
        name=lst.name,
        description=lst.description
    )
    created_list = crud.create_list(db, db_lst)

    return created_list

@router.delete('/lists/{list_id}')
def delete_list(list_id: int, db: Session = Depends(get_db)):
    lst = crud.get_list(db, list_id)
    crud.delete_list(db, list_id)
    return lst


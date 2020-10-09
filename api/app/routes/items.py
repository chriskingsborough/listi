from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .database import models, schemas, crud
from .database.database import engine
from .utils import get_db
from typing import List

router = APIRouter()

# database operations
models.Base.metadata.create_all(bind=engine)

@router.get('/lists/{list_id}/items')
def get_items(list_id: int, db: Session = Depends(get_db)):
    items = crud.get_items(db, list_id)
    return items

@router.post('/lists/{list_id}/items')
def post_items(list_id: int, items: List[schemas.Item], db: Session = Depends(get_db)):
    return items
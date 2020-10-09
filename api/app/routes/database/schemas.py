"""Define pydantic schemas"""
from pydantic import BaseModel
from typing import Optional, List

# define the list model
class List(BaseModel):
    list_id: Optional[int] = None
    name: str
    user_id: int
    description: Optional[str] = None

    class Config:
        orm_mode = True

class Item(BaseModel):
    item_id: Optional[int] = None
    list_id: int
    user_id: int
    field_name: str
    field_value: str
    is_detail: bool

    class Config:
        orm_mode = True
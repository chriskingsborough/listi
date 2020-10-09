### Create database tables ###

from sqlalchemy import Column, Integer, String, Date, DateTime, JSON, Text, Boolean
from sqlalchemy.orm import relationship
from .database import Base

# TODO: add table relationships
# TODO: update indexes


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String)
    phone_number = Column(String)
    password = Column(String)

class UserLists(Base):
    __tablename__ = 'user_lists'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    list_id = Column(Integer)
    role_id = Column(Integer)

class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    privileges = Column(JSON)

class Lists(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    description = Column(Text)

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    list_id = Column(Integer)
    field_values = Column(JSON)

class ItemFields(Base):
    __tablename__ = 'item_fields'
    id = Column(Integer, primary_key=True, index=True)
    list_id = Column(Integer)
    field_name = Column(String)
    is_detail = Column(Boolean)
    field_order = Column(Integer)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    list_id = Column(Integer)
    item_id = Column(Integer)
    comment = Column(Text)
    created = Column(DateTime)
    last_updated = Column(DateTime)

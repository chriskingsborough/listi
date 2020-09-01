### Create database tables ###

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, JSON, Text, Boolean
from sqlalchemy import create_engine

Base = declarative_base()

database_uri = 'postgres+psycopg2://admin:admin@localhost:5432/listi'

engine = create_engine(database_uri)

Base.metadata.drop_all(engine)

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String)
    phone_number = Column(String)
    password = Column(String)

class UserLists(Base):
    __tablename__ = 'user_lists'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    list_id = Column(Integer)
    role_id = Column(Integer)

class Roles(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    privileges = Column(JSON)

class Lists(Base):
    __tablename__ = 'lists'
    list_id = Column(Integer, primary_key=True)
    description = Column(Text)

class Items(Base):
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True)
    list_id = Column(Integer)
    field_values = Column(JSON)

class ItemFields(Base):
    __tablename__ = 'item_fields'
    id = Column(Integer, primary_key=True)
    list_id = Column(Integer)
    field_name = Column(String)
    is_detail = Column(Boolean)

class Comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    list_id = Column(Integer)
    item_id = Column(Integer)
    comment = Column(Text)
    created = Column(DateTime)
    last_updated = Column(DateTime)



if __name__ == '__main__':
    Base.metadata.create_all(engine)
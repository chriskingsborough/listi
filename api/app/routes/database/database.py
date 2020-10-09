from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost/listi"
SQLALCHEMY_DATABASE_URL = "postgres://neefjvqilhgatg:cc9342875dc38280cb275a26f4bcc4546cf1582fae929a0a895b9630c71834f8@ec2-3-214-46-194.compute-1.amazonaws.com:5432/d9k5gv2j90sgs8"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()
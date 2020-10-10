from .database.database import SessionLocal

# dependency
# not sure if this will work but its duped here.. 
# seems to be working - deleted from the other place

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

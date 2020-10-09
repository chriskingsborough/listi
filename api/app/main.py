from fastapi import FastAPI

from typing import Optional
from routes import lists, items
from routes.database import models
from routes.database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(lists.router)
app.include_router(items.router)
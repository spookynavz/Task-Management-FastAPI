from app.database import Base, engine, get_db
from fastapi import FastAPI, Depends, HTTPException
from app.router import auth, task


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task.router)
app.include_router(auth.router)

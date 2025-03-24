from app.database import Base, engine
from fastapi import FastAPI
from app.router import auth, task, feedback


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(feedback.router, prefix="/api")

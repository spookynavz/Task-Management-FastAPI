from typing import Union, List
from sqlalchemy.orm import Session
from . import models, schemas
import app.router.auth
# from app.database import Base, engine, get_db
# from fastapi import FastAPI, Depends, HTTPException
# from app.models.task import Task as TaskModel
# from app.schemas.task import Task as TaskSchema
import json

# Base.metadata.create_all(bind=engine)

# app = FastAPI()






# @app.get("/task")
# def get_task():
#     with open("task.json","r") as file:
#         task_data = json.load(file)
#     return task_data


from typing import Union
from app.routers.task import router as task_router
#from APP.schemas.models import 
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/task")
def get_task():
    with open("task.json","r") as file:
        task_data = json.load(file)
    return task_data


from typing import Union
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/task")
def get_task():
    with open("task.json","r") as file:
        task_data = json.load(file)
    return task_data

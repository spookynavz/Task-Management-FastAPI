from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app import models, schemas
from app.database import get_db
from app.models.task import Task as TaskModel
from app.schemas.task import Task as TaskSchema
from app.dao.task import create_task, update_task, delete_task, get_tasks, get_task_by_id


router = APIRouter(prefix='/task', tags=['task'])


@router.post("/create", response_model=TaskSchema)
def creation(task:TaskSchema, db:Session = Depends(get_db)):
    return create_task(db, task)


    
@router.get("/retrieve", response_model=List[TaskSchema])
def retrieve_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip, limit)

@router.get("/{task_id}", response_model=TaskSchema)
def retrieve_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task



@router.put("/update/{task_id}", response_model=TaskSchema)
def updating(task_id: int, task: TaskSchema, db: Session = Depends(get_db)):
    updated_task = update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task



@router.delete("/delete/{task_id}")
def deletion(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app import models, schemas
from app.database import get_db
from app.models.task import Task as TaskModel
from app.schemas.task import Task as TaskSchema

from datetime import date

router = APIRouter()


@router.post("/task", response_model=TaskSchema)
def create_task(task:TaskSchema, db:Session = Depends(get_db)):
    db_task = TaskModel(
        title=task.title,
        description=task.description,
        start_date=task.start_date if task.start_date else date.today(),
        end_date=task.end_date,
        assigned_by_id=task.assigned_by_id,
        assigned_to_id=task.assigned_to_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


    
@router.get("/tasks/", response_model=List[TaskSchema])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).offset(skip).limit(limit).all()
    return tasks



@router.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task: TaskSchema, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update attributes dynamically
    task_data = vars(task)
    for key, value in task_data.items():
        if hasattr(db_task, key) and value is not None:
            setattr(db_task, key, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task




@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}

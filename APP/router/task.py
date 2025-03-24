from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.database import get_db
from app.schemas.task import Task as TaskSchema
from app.dao.task import create_task, update_task, delete_task, get_tasks, get_task_by_id
from app.middlewares.auth import auth_required, manager_required, admin_required


router = APIRouter(prefix='/task', tags=['task'])


@router.post("/create", response_model=TaskSchema)
def creation(task:TaskSchema, db:Session = Depends(get_db), current_user=Depends(manager_required)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    #print(f"DEBUG: Authenticated User ID - {current_user.id}, Role - {current_user.role}")

    task_data = task.model_dump()
    task_data["assigned_by_id"] = current_user.id

    #print(f"DEBUG: Task Data Before Saving - {task_data}")

    return create_task(db, **task_data)


    
@router.get("/retrieve", response_model=List[TaskSchema])
def retrieve_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user=Depends(auth_required)):
    return get_tasks(db, skip, limit)

@router.get("/{task_id}", response_model=TaskSchema)
def retrieve_task_by_id(task_id: int, db: Session = Depends(get_db), current_user=Depends(auth_required)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task



@router.put("/update/{task_id}", response_model=TaskSchema)
def updating(task_id: int, task: TaskSchema, db: Session = Depends(get_db), current_user=Depends(auth_required)):
    updated_task = update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task



@router.delete("/delete/{task_id}")
def deletion(task_id: int, db: Session = Depends(get_db), current_user=Depends(manager_required)):
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"} 
from sqlalchemy.orm import Session
from app.schemas.feedback import FeedbackCreate
from app.models.feedback import Feedback
from app.models.task import Task
from fastapi import HTTPException, status

def create_feedback(db: Session, feedback_data: FeedbackCreate):
    db_task = db.query(Task).filter(Task.id == feedback_data.task_id).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    new_feedback = Feedback(**feedback_data.model_dump())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback

def get_feedback_by_task(db: Session, task_id: int):
    return db.query(Feedback).filter(Feedback.task_id == task_id).all()
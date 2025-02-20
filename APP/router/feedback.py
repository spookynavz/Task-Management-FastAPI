from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.models.task import Task
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.dao.feedback import create_feedback, get_feedback_by_task

router = APIRouter(prefix="/feedback", tags=["feedback"])

@router.post("/create/{task_id}", response_model=FeedbackResponse)
def add_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    new_feedback = create_feedback(db, feedback)
    if not new_feedback:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return new_feedback



@router.get("/retrieve/{task_id}", response_model=list[FeedbackResponse])
def retrieve_feedback(task_id: int, db: Session = Depends(get_db)):
    feedbacks = get_feedback_by_task(db, task_id)
    if not feedbacks:
        raise HTTPException(status_code=404, detail="No feedback found for this task")
    return feedbacks
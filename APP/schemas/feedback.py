from pydantic import BaseModel
from typing import Optional
from datetime import date

class FeedbackCreate(BaseModel):
    task_id: int
    manager_id: int
    feedback: str
    status: str

class FeedbackResponse(FeedbackCreate):
    id: int

    class Config:
        orm_mode = True
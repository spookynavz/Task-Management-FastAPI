from pydantic import BaseModel
from typing import Optional, List

# Schema for Task
class TaskBase(BaseModel):
    title: str
    description: Optional[str]

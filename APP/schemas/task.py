from pydantic import BaseModel
from typing import Optional, List

# Schema for Task
class Task(BaseModel):
    title: str
    description: Optional[str]

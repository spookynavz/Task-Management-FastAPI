from pydantic import BaseModel
from datetime import date
from typing import Optional


class Task(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    description: Optional[str]=None
    start_date: Optional[date]=None
    end_date: Optional[date]=None
    assigned_by_id: Optional[int]=None
    assigned_to_id: Optional[int]=None

    class Config:
        orm_mode = True

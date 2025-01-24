from pydantic import BaseModel
from datetime import date
from sqlmodel import SQLModel, Field

# this is the base class
class project_base(SQLModel):
    name : str
    start_date : date
    end_date : date
    description : str

#this is a db table, and is inherited from the baseclass
class project(project_base, table=True):
    id : int = Field(default=None, primary_key=True)
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker
from database import Base
from datetime import date

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(str)
    email = Column(str, unique=True, index=True)

    # Relationships
    tasks_assigned = relationship("Task", foreign_keys="Task.assigned_by_id", back_populates="assigned_by")
    tasks_received = relationship("Task", foreign_keys="Task.assigned_to_id", back_populates="assigned_to")
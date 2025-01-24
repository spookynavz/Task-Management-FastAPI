from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(str)
    email = Column(str, unique=True, index=True)

    # Relationships
    tasks_assigned = relationship("Task", foreign_keys="Task.assigned_by_id", back_populates="assigned_by")
    tasks_received = relationship("Task", foreign_keys="Task.assigned_to_id", back_populates="assigned_to")

# Task Model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(str)
    description = Column(str)
    start_date = date
    end_date : date
    assigned_by_id = Column(Integer, ForeignKey("users.id"))
    assigned_to_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    assigned_by = relationship("User", foreign_keys=[assigned_by_id], back_populates="tasks_assigned")
    assigned_to = relationship("User", foreign_keys=[assigned_to_id], back_populates="tasks_received")

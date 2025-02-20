from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker
from app.database import Base
from datetime import date

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    added_at = Column(DateTime)
    updated_at = Column(DateTime)

    # Relationships
    tasks_assigned = relationship("Task", foreign_keys="Task.assigned_by_id", back_populates="assigned_by")
    tasks_received = relationship("Task", foreign_keys="Task.assigned_to_id", back_populates="assigned_to")
    manager_feedbacks = relationship("Feedback", back_populates="manager")
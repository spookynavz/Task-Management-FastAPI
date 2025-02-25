from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class RoleEnum(str, enum.Enum): 
    ADMIN = "Admin"
    MANAGER = "Manager"
    EMPLOYEE = "Employee"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.EMPLOYEE)
    added_at = Column(DateTime)
    updated_at = Column(DateTime)

    # Relationships
    tasks_assigned = relationship("Task", foreign_keys="Task.assigned_by_id", back_populates="assigned_by")
    tasks_received = relationship("Task", foreign_keys="Task.assigned_to_id", back_populates="assigned_to")
    manager_feedbacks = relationship("Feedback", back_populates="manager")
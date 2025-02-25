from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base


# Task Model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    assigned_by_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    assigned_to_id = Column(Integer, ForeignKey("users.id"))


    # Relationships
    assigned_by = relationship("User", foreign_keys=[assigned_by_id], back_populates="tasks_assigned")
    assigned_to = relationship("User", foreign_keys=[assigned_to_id], back_populates="tasks_received")
    feedbacks = relationship("Feedback", back_populates="task", cascade="all, delete")


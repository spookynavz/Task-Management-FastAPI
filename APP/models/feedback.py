from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id= Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    reviewer = Column(Integer, ForeignKey("users.id"))
    feedback = Column(String)
    status = Column(String)

    task = relationship("Task", back_populates="feedbacks")
    manager = relationship("User", back_populates="manager_feedbacks")
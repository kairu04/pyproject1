# The app's database.
from database import Base
from sqlalchemy import Column, String, Boolean, Integer, DateTime, Text


class Task(Base):
    __tablename__: str = 'tasks'
    task_id = Column(Integer, primary_key=True)
    category = Column(String(255), nullable=False, unique=True)
    activity = Column(Text)
    status = Column(Boolean, default=False)
    date_created = Column(DateTime)

    def __repr__(self):
        return f'<Task activity={self.activity} >'

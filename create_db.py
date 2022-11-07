from database import Base , Engine
from models import Task

Base.metadata.create_all(Engine)

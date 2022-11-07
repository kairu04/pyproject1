from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import datetime

import models
from database import LocalSession

app = FastAPI()
session = LocalSession()


# serializer
class Task(BaseModel):
    task_id: int
    category: str
    activity: str
    status: bool
    date_created: datetime.datetime.utcnow

    class config:
        orm_mode = True


@app.get('/tasks', reponse_model=List[Task], status_code=200)
def index():
    """Homepage for app. Lists all the user-created tasks and a delete action."""
    return session.query(models.Task).all()


@app.get('/tasks/{task_id}', response_model=List[Task], status_code=200)
def edit_task(task_id: int):
    """Pop-up page when user clicks on task."""
    if task_id == session.query(models.Task).get(task_id):
        return 0


@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    """Updates a task in the database."""
    return {"Update task.": "Update task."}


@app.post("/task")
def create_task():
    """Pop-up when user clicks 'create task' button. Saves task into database."""
    return {"Create task": "Create task."}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Deletes a task when user clicks a delete button in the edit pop-up or on homepage."""
    return {"Delete task.": "Delete task."}

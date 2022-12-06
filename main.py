from fastapi import FastAPI, status
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

    class Config:
        orm_mode = True


db = LocalSession()


@app.get('/tasks', response_model = List[Task], status_code = 200)
def index():
    #"""Homepage for app. Lists all the user-created tasks and a delete action."""
    tasks = db.query(models.Task).all()

    return tasks


#"""Pop-up page when user clicks on task."""

@app.get('/tasks/{task_id}', response_model=Task, status_code=status.HTTP_200_OK)
def get_task(task_id: int):
    task=db.query(models.Task)
    if task_id == session.query(models.Task).get(task_id):
        return 0


 #"""Pop-up when user clicks 'create task' button. Saves task into database."""
@app.post("/task", response_model = Task,
          status_code=status.HTTP_201_CREATED)
def create_task(task:Task):
    new_task=models.Task(
        category = task.category,
        activity = task.activity,
        status = task.status,
    )

    db_item = db.query(models.Task).filter(task.name==new_task.name).first()

    if db_task is not None:
        raise HttpException(status_code=400,detail="Similar task already exists")

    db.add(new_task)
    db.commit()

    return new_task

#Updates a task in the database.
@app.put("/tasks/{task_id}", response_model=Task, status_code = status.HTTP_200_OK)
def update_task(task_id:int,item:Item):
    task_to_update=db.query(models.Task).filter(models.Task.id==task_id).first()
    task_to_update.activity=task.activity
    task_to_update.description=task.description
    task_to_update.status=task.status

    db.commit()
    return task_to_update


#Deletes a task when user clicks a delete button in the edit pop-up or on homepage."""

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_to_delete=db.query(models.Task).filter(models.Task.id==task_id).first()

    if task_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(task_to_delete)
    db.commit()

    return task_to_delete



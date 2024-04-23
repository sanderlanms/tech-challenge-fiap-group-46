from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str

tasks=[]


@app.get('/')
async def hello_api():
    return {'Olá, essa é minha api'}

@app.get('/tasks')
async def read_tasks():
    return {'tasks: ':tasks}

@app.post('/tasks', status_code=201)
async def create_task(task:Task):
    tasks.append(task)
    return task

@app.delete('/tasks/{task_id}', status_code=204)
async def delete_task(task_id:int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]

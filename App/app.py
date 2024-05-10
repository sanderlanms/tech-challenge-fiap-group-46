
from fastapi import FastAPI
from pydantic import BaseModel
#from Classes.comercializacao import FileComercializacao as fc
#import Classes.comercializacao as co

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
""""
@app.get('/files/{url}')
async def read_data(url: str):
    dados = {
        "path": "",
        "fileName": "comercializacao.csv",
        "url": url
    }
    #fileComercializacao = co.FileComercializacao(**dados)
    #listaRetornoCSV = fileComercializacao.LerCsv()
    #return {'Data:':listaRetornoCSV[1]}
    return {'dados':co.FileComercializacao(**dados).LerCsv()}
"""
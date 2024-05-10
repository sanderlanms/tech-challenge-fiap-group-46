
from fastapi import FastAPI


#from Classes.comercializacao import FileComercializacao as fc
#import Classes.comercializacao as com
#import Classes
#import Classes.comercializacao
#from Classes.comercializacao import *
#from Classes.comercializacao import FileComercializacao as comerc
#from .Classes.comercializacao import *
from comercializacao import FileComercializacao

api = FastAPI()

""""
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
"""
@api.get('/')
async def hello_api():
    return {'Olá, essa é minha api'}


@api.get('/files')
def read_data():
    dados = {
        "path": "",
        "fileName": "comercializacao.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    }
    fileComercializacao = FileComercializacao(**dados)
    listaRetornoCSV = fileComercializacao.LerCsv()
    print(listaRetornoCSV)
    return {'Data:':listaRetornoCSV[1]}
    #return {'dados':co.FileComercializacao(**dados).LerCsv()}
    #return {'dados': dados}

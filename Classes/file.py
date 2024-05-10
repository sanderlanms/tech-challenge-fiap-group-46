import pandas as pd
from typing import List
from pydantic import BaseModel


class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float


class Retorno(BaseModel):
    Id: int
    Produto: str
    Dados: List[RetornoAuxiliar]

class File:

    path = None
    file = None

    def __init__(self,path):
        self.path = path

    def uploadFile(self):
        self.file = pd.read_csv(self.path,sep=';')

    def getFile(self):
        return self.file


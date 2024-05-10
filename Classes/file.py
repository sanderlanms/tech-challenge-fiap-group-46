import os
import urllib.request
from pathlib import Path
import pandas as pd
from typing import List
from pydantic import BaseModel

_basePath = '../csv/'

class RetornoAuxiliar(BaseModel):
    Ano: int
    Valor: float

class Retorno(BaseModel):
    Id: int
    Nome: str
    NomeAmigavel: str
    Dados: List[RetornoAuxiliar]

class File(BaseModel):

    path: str
    fileName: str
    url: str

    #retorno = Retorno
    #retornoAuxiliar = RetornoAuxiliar

    def setAttributes(self):
            self.path = '../csv/' + self.fileName
    def setFilePath(self,url):
        self.url = url

    def uploadFile(self):
        self.fileName = pd.read_csv(self.path,sep=';')

    def getFile(self):
        return self.fileName

    def GetCsv(url, name):
        my_file = Path(name)
        if my_file.is_file():
            return

        if not os.path.exists(_basePath):
            os.makedirs(_basePath)
        urllib.request.urlretrieve(url, _basePath+name)

    def ReadCsv(self,fileName, removeHeader=False):
        self.setAttributes()
        with open(self.path, 'r', encoding='UTF-8') as file:
            if (removeHeader):
                return [line.strip().replace('\t', ';') for line in file if line.strip() != ''][1:]
            return [line.strip().replace('\t', ';') for line in file if line.strip() != '']
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

class RetornoExportacao(BaseModel):
    Id: int
    Pais: str
    TipoProduto: str
    Dados: List[RetornoAuxiliar]

class RetornoImportacao(BaseModel):
    Id: int
    Nome: str
    NomeAmigavel: str
    TipoProduto: str
    Dados: List[RetornoAuxiliar]

class RetornoProducao(BaseModel):
    Id: int
    Produto: str
    Dados: List[RetornoAuxiliar]

class File(BaseModel):
    path: str
    fileName: str
    url: str
    list: List

    #retorno = Retorno
    #retornoAuxiliar = RetornoAuxiliar

    def setAttributePath(self):
        self.path = '../csv/' + self.fileName

    def setAttributeList(self,list_):
        self.list =  list_

    #def setFilePath(self,url):
        #self.url = url

    #def uploadFile(self):
        #self.fileName = pd.read_csv(self.path,sep=';')

    #def getFile(self):
        #return self.fileName

    def download_csv(self):
        #File.GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv', self._fileNameProd)
        self.get_csv()

    def get_csv(self):
    # def get_csv(url, name):
        my_file = Path(self.fileName)
        if my_file.is_file():
            return

        if not os.path.exists(_basePath):
            os.makedirs(_basePath)
        urllib.request.urlretrieve(self.url, _basePath+self.fileName)

    def read_csv(self,fileName, removeHeader=False):
        self.setAttributePath()
        with open(self.path, 'r', encoding='UTF-8') as file:
            if (removeHeader):
                return [line.strip().replace('\t', ';') for line in file if line.strip() != ''][1:]
            return [line.strip().replace('\t', ';') for line in file if line.strip() != '']
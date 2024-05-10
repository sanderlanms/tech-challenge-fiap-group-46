from typing import List
from pydantic import BaseModel
from file import *

#from Utils.Utils import GetCsv, ReadCsv

#_fileNameProd = 'comercializacao.csv'

class FileComercializacao(File):

    def download_csv(self,url):
        #File.GetCsv('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv', self._fileNameProd)
        File.GetCsv(self.url, self.fileName)

    def LerCsv(self):
        self.download_csv(self.url)
        csv = self.ReadCsv(self.fileName,True)
        csv_colunas = ['Id', 'Nome', 'Nome Amigavel'] + [x for x in range(1970, 2023)]
        lista = []
        for i in range(0, len(csv)):
            csv_linha = csv[i].split(';')
            retorno = Retorno(Id=csv_linha[0], Nome=csv_linha[1],NomeAmigavel=csv_linha[2].strip(), Dados=[])
            for j in range(3, len(csv_colunas)):
                retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j]))
            lista.append(retorno)
        return lista

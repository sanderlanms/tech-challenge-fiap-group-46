#from typing import List
#from pydantic import BaseModel
from file import *

#from Utils.Utils import GetCsv, ReadCsv

#_fileNameProd = 'comercializacao.csv'

class FileComercializacao(File):

    #def LerCsv(self):
    def get_list_by_csv(self):
        self.download_csv()
        csv = self.read_csv(self.fileName,True)
        csv_colunas = ['Id', 'Nome', 'Nome Amigavel'] + [x for x in range(1970, 2023)]
        lista = []
        for i in range(0, len(csv)):
            csv_linha = csv[i].split(';')
            retorno = Retorno(Id=csv_linha[0], Nome=csv_linha[1],NomeAmigavel=csv_linha[2].strip(), Dados=[])
            for j in range(3, len(csv_colunas)):
                retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j]))
            lista.append(retorno)
        self.setAttributeList(lista)
        return lista

    """def find(self,month,year):
        retorno = self.list
        return retorno"""
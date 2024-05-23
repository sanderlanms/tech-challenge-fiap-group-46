from file import *

class FileProducao(File):

    def get_list_by_csv(self):
        self.download_csv()
        csv = self.read_csv(self.fileName)
        csv_colunas = csv[0].split(';')
        lista = []
        for i in range(1, len(csv)):
            csv_linha = csv[i].split(';')
            retorno = RetornoProducao(Id=csv_linha[0], Produto=csv_linha[1], Dados=[])
            for j in range(3, len(csv_colunas)):
                retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j]))
            lista.append(retorno)
        self.setAttributeList(lista)
        return lista

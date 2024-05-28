from Classes.utils import File, RetornoExportacao, RetornoAuxiliar

class FileImportacao(File):

    def ordernar_por_nome(linha):
        return linha.lower().split('\t')[1]

    def get_list_by_csv(self,tipoProduto):
        self.download_csv()

        lista = []
        csv = self.read_csv(self.fileName,False)
        csv_colunas = csv[0].split(';')
        for i in range(1, len(csv)):
            csv_linha = csv[i].split(';')
            retorno = RetornoExportacao(Id=csv_linha[0], Pais=csv_linha[1], TipoProduto=tipoProduto, Dados=[])
            for j in range(2, len(csv_colunas)):
                retorno.Dados.append(RetornoAuxiliar(Ano=csv_colunas[j], Valor=csv_linha[j] if csv_linha[j] != '' else 0))
            lista.append(retorno)
        return lista

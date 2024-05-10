from file import File

# fileComercio = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/Comercio.csv')
# fileExpEspumantes = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ExpEspumantes.csv')
# fileExpSuco = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ExpSuco.csv')
# fileExpUva = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ExpUva.csv')
# fileExpVinho = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ExpVinho.csv')
# fileImpEspumantes = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ImpEspumantes.csv')
# fileImpFrescas = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ImpFrescas.csv')
# fileImpPassas = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ImpPassas.csv')
# fileImpSuco = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ImpSuco.csv')
# fileImpVinhos = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ImpVinhos.csv')
# fileProcessaAmericanas = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ProcessaAmericanas.csv')
# fileProcessaMesa = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ProcessaMesa.csv')
# fileProcessaSemclass = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ProcessaSemclass.csv')
# fileProcessaViniferas = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/ProcessaViniferas.csv')
# fileProducao = File('D:/Estudos/Pos_Graduacao_FIAP/Modulo_1/tech_challenge/Producao.csv')
#
# fileComercio.uploadFile()
# fileExpEspumantes.uploadFile()
# fileExpSuco.uploadFile()
# fileExpUva.uploadFile()
# fileExpVinho.uploadFile()
# fileImpEspumantes.uploadFile()
# fileImpFrescas.uploadFile()
# fileImpPassas.uploadFile()
# fileImpSuco.uploadFile()
# fileImpVinhos.uploadFile()
# fileProcessaAmericanas.uploadFile()
# fileProcessaMesa.uploadFile()
# fileProcessaSemclass.uploadFile()
# fileProcessaViniferas.uploadFile()
# fileProducao.uploadFile()



# print(fileComercio.getFile().head())
# print(fileExpEspumantes.getFile().head())
# print(fileExpSuco.getFile().head())
# print(fileExpUva.getFile().head())
# print(fileExpVinho.getFile().head())
# print(fileImpEspumantes.getFile().head())
# print(fileImpFrescas.getFile().head())
# print(fileImpPassas.getFile().head())
# print(fileImpSuco.getFile().head())
# print(fileImpVinhos.getFile().head())
# print(fileProcessaAmericanas.getFile().head())
# print(fileProcessaMesa.getFile().head())
# print(fileProcessaSemclass.getFile().head())
# print(fileProcessaViniferas.getFile().head())
# print(fileProducao.getFile().head())



from typing import List
from pydantic import BaseModel
from comercializacao import FileComercializacao

dados = {
    "path": "",
    "fileName": "comercializacao.csv",
    "url": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
}
fileComercializacao = FileComercializacao(**dados)
#fileComercializacao.setAttributes(path='',newFileName='producaoNew.csv',url='http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv')
#fileComercializacao = FileComercializacao(path='',fileName='producaoNew.csv',url='http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv')
#fileComercializacao.setFileName('producaoNew.csv')
#fileComercializacao.DownloadCsv('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv')
listaRetornoCSV = fileComercializacao.LerCsv()
print(listaRetornoCSV[0])
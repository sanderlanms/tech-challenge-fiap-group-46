from comercializacao import FileComercializacao
from exportacao import FileExportacao
from processamento import FileProcessamento
from producao import FileProducao

dadosComercializacao = {
    "path": "",
    "fileName": "comercializacao.csv",
    "url": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
    "list": []
}
fileComercializacao = FileComercializacao(**dadosComercializacao)
listaRetornoCSV = fileComercializacao.get_list_by_csv()
print('__________________COMERCIALIZACAO___________________')
print(listaRetornoCSV[0])
print('____________________________________________________')

dadosExportacaoVinhos = {
        "path": "",
        "fileName": "ExportacaoVinhos.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "list": []
    }

dadosExportacaoEspumantes = {
        "path": "",
        "fileName": "ExportacaoEspumantes.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "list": []
    }

dadosExportacaoFrescas = {
        "path": "",
        "fileName": "ExportacaoFrescas.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "list": []
    }

dadosExportacaoSucos = {
        "path": "",
        "fileName": "ExportacaoSucos.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "list": []
    }

listExportacao = {"Vinhos": dadosExportacaoVinhos
, "Espumantes": dadosExportacaoEspumantes
, "Uvas_Frescas": dadosExportacaoFrescas
, "Sucos": dadosExportacaoSucos
}


listaRetornoExportacaoCSV = []

for key, val in listExportacao.items():
    fileExportacao = FileExportacao(**val)
    listaRetornoExportacaoCSV.append(fileExportacao.get_list_by_csv(key))
    #print(key)
print('_____________________EXPORTACAO_____________________')
print(listaRetornoExportacaoCSV[0][1])
print(listaRetornoExportacaoCSV[1][1])
print(listaRetornoExportacaoCSV[2][1])
print(listaRetornoExportacaoCSV[3][1])
print('____________________________________________________')




dadosImportacaoVinhos = {
        "path": "",
        "fileName": "ImportacaoVinhos.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "list": []
    }
dadosImportacaoEspumantes = {
        "path": "",
        "fileName": "ImportacaoEspumantes.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "list": []
    }
dadosImportacaoFrescas = {
        "path": "",
        "fileName": "ImportacaoFrescas.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "list": []
    }
dadosImportacaoPassas = {
        "path": "",
        "fileName": "ImportacaoPassas.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "list": []
    }
dadosImportacaoSucos = {
        "path": "",
        "fileName": "ImportacaoSucos.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "list": []
    }
listImportacao = {"Vinhos": dadosImportacaoVinhos
                    , "Espumantes": dadosImportacaoEspumantes
                    , "Uvas_Frescas": dadosImportacaoFrescas
                    , "Uvas_Passadas": dadosImportacaoPassas
                    , "Sucos": dadosImportacaoSucos
                }


listaRetornoImportacaoCSV = []

for key, val in listImportacao.items():
    fileImportacao = FileExportacao(**val)
    listaRetornoImportacaoCSV.append(fileImportacao.get_list_by_csv(key))
    #print(key)
print('_____________________IMPORTACAO_____________________')
print(listaRetornoImportacaoCSV[0][1])
print(listaRetornoImportacaoCSV[1][1])
print(listaRetornoImportacaoCSV[2][1])
print(listaRetornoImportacaoCSV[3][1])
print(listaRetornoImportacaoCSV[4][1])
print('____________________________________________________')


dadosProcessaViniferas = {
        "path": "",
        "fileName": "ProcessaViniferas.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "list": []
    }
dadosProcessaAmericanas = {
        "path": "",
        "fileName": "ProcessaAmericanas.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "list": []
    }
dadosProcessaMesa = {
        "path": "",
        "fileName": "ProcessaMesa.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "list": []
    }
dadosProcessaSemclass = {
        "path": "",
        "fileName": "ProcessaSemclass.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "list": []
    }

listProcessamento = {"Viniferas": dadosProcessaViniferas
                    ,"Americanas": dadosProcessaAmericanas
                    ,"Mesa": dadosProcessaMesa
                    ,"SemClasse": dadosProcessaSemclass
                }


listaRetornoProcessamentoCSV = []

for key, val in listProcessamento.items():
    fileProcessamento = FileProcessamento(**val)
    listaRetornoProcessamentoCSV.append(fileProcessamento.get_list_by_csv(key))
    #print(key)
print('___________________PROCESSAMENTO____________________')
print(listaRetornoProcessamentoCSV[0][1])
print(listaRetornoProcessamentoCSV[1][1])
print(listaRetornoProcessamentoCSV[2][1])
print(listaRetornoProcessamentoCSV[3][0])
print('____________________________________________________')



dadosProducao = {
    "path": "",
    "fileName": "prod.csv",
    "url": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "list": []
}
fileProducao = FileProducao(**dadosProducao)
listaRetornoProducaoCSV = fileProducao.get_list_by_csv()
print('_____________________PRODUCAO_______________________')
print(listaRetornoProducaoCSV[0])
print('____________________________________________________')

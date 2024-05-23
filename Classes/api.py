from fastapi import FastAPI
from comercializacao import FileComercializacao
from exportacao import FileExportacao
from importacao import FileImportacao
from processamento import FileProcessamento
from producao import FileProducao

api = FastAPI()
dadosComercializacao = {
        "path": "",
        "fileName": "comercializacao.csv",
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "list": []
    }
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
                    ,"Espumantes": dadosExportacaoEspumantes
                    ,"Uvas_Frescas": dadosExportacaoFrescas
                    ,"Sucos": dadosExportacaoSucos
                }


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
dadosProducao = {
    "path": "",
    "fileName": "prod.csv",
    "url": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
    "list": []
}

@api.get('/')
async def hello_api():
    return {'Olá, essa é minha api'}


@api.get('/comercializacaoList')
def list_comercializacao():
    fileComercializacao = FileComercializacao(**dadosComercializacao)
    listaRetornoComercializacaoCSV = fileComercializacao.get_list_by_csv()
    print(listaRetornoComercializacaoCSV[1])
    return {'Data:':listaRetornoComercializacaoCSV[1]}
    #return {'dados':co.FileComercializacao(**dados).LerCsv()}
    #return {'dados': dados}

@api.get('/comercializacaoFind')
def find_comercializacao():
    fileComercializacao = FileComercializacao(**dadosComercializacao)
    listaRetornoCSV = fileComercializacao.get_list_by_csv()
    return {'Data:': listaRetornoCSV[1]}


@api.get('/exportacaoList')
def list_exportacao():

    listaRetornoExportacaoCSV = []
    for key, val in listExportacao.items():
        fileExportacao = FileExportacao(**val)
        listaRetornoExportacaoCSV.append(fileExportacao.get_list_by_csv(key))
    print(listaRetornoExportacaoCSV[0][1])
    print(listaRetornoExportacaoCSV[1][1])
    print(listaRetornoExportacaoCSV[2][1])
    print(listaRetornoExportacaoCSV[3][1])
    retorno = []
    retorno.append(listaRetornoExportacaoCSV[0][1])
    retorno.append(listaRetornoExportacaoCSV[1][1])
    retorno.append(listaRetornoExportacaoCSV[2][1])
    retorno.append(listaRetornoExportacaoCSV[3][1])
    return {'Data:':retorno}


@api.get('/importacaoList')
def list_importacao():
    listaRetornoImportacaoCSV = []
    for key, val in listImportacao.items():
        fileImportacao = FileImportacao(**val)
        listaRetornoImportacaoCSV.append(fileImportacao.get_list_by_csv(key))
    print(listaRetornoImportacaoCSV[0][1])
    print(listaRetornoImportacaoCSV[1][1])
    print(listaRetornoImportacaoCSV[2][1])
    print(listaRetornoImportacaoCSV[3][1])
    print(listaRetornoImportacaoCSV[4][1])
    retornoImportacao = []
    retornoImportacao.append(listaRetornoImportacaoCSV[0][1])
    retornoImportacao.append(listaRetornoImportacaoCSV[1][1])
    retornoImportacao.append(listaRetornoImportacaoCSV[2][1])
    retornoImportacao.append(listaRetornoImportacaoCSV[3][1])
    retornoImportacao.append(listaRetornoImportacaoCSV[4][1])
    return {'Data:':retornoImportacao}

@api.get('/processamentoList')
def list_processamento():
    listaRetornoProcessamentoCSV = []
    for key, val in listProcessamento.items():
        fileProcessamento = FileProcessamento(**val)
        listaRetornoProcessamentoCSV.append(fileProcessamento.get_list_by_csv(key))
    print(listaRetornoProcessamentoCSV[0][1])
    print(listaRetornoProcessamentoCSV[1][1])
    print(listaRetornoProcessamentoCSV[2][1])
    print(listaRetornoProcessamentoCSV[3][0])
    retornoProcessamento = []
    retornoProcessamento.append(listaRetornoProcessamentoCSV[0][1])
    retornoProcessamento.append(listaRetornoProcessamentoCSV[1][1])
    retornoProcessamento.append(listaRetornoProcessamentoCSV[2][1])
    retornoProcessamento.append(listaRetornoProcessamentoCSV[3][0])
    return {'Data:':retornoProcessamento}

@api.get('/producaoList')
def list_producao():
    fileProducao = FileProducao(**dadosProducao)
    listaRetornoProducaoCSV = fileProducao.get_list_by_csv()
    print(listaRetornoProducaoCSV[1])
    return {'Data:':listaRetornoProducaoCSV[1]}

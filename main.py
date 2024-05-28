from fastapi import FastAPI
from Classes.comercializacao import FileComercializacao
from Classes.exportacao import FileExportacao
from Classes.importacao import FileImportacao
from Classes.processamento import FileProcessamento
from Classes.producao import FileProducao

app = FastAPI()
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

@app.get('/')
async def hello_api():
    return {'Olá, essa é minha API! Para documentaçao, digite /docs# na rota.'}


@app.get('/comercializacaoList')
def list_comercializacao():
    """
    Retorna dados de comercializaçao de vinhos e derivados no Rio Grande do Sul.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Nome": "VINHO DE MESA",
            "NomeAmigavel": "VINHO DE MESA",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 98327606
            },
            ...
            ]
        }
    ]
    ```
    """
    fileComercializacao = FileComercializacao(**dadosComercializacao)
    listaRetornoComercializacaoCSV = fileComercializacao.get_list_by_csv()
    print(listaRetornoComercializacaoCSV[1])
    return {'Data:':listaRetornoComercializacaoCSV[1]}


@app.get('/comercializacaoFind')
def find_comercializacao():
    fileComercializacao = FileComercializacao(**dadosComercializacao)
    listaRetornoCSV = fileComercializacao.get_list_by_csv()
    return {'Data:': listaRetornoCSV[1]}


@app.get('/exportacaoList')
def list_exportacao():
    """
    Retorna dados de exportaçao de derivados de uva.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "id": 36,
            "País": Mônaco
            "Dados": [
            {
                "Quantidade": 1180759,
                "Valor": 512716
            }
            ...
            ]
        }
    ]
    ```
    """
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


@app.get('/importacaoList')
def list_importacao():
    """
    Retorna dados de importação de derivados de uva.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Pais": "Africa do Sul",
            "TipoProduto": "Vinhos",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 0
            },
            ...
            ]
        }
    ]
    ```
    """
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

@app.get('/processamentoList')
def list_processamento():
    """
    Retorna dados de quantidade de uvas processadas no Rio Grande do Sul.


    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Nome": "TINTAS",
            "NomeAmigavel": "TINTAS",
            "TipoProduto": "Viniferas",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 10448228
            },
            ...
            ]
        }
    ]
    ```
    """
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

@app.get('/producaoList')
def list_producao():
    """
    Retorna dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.

    Exemplo de chamada:
    ```
    GET /producaoList
    ```

    Exemplo de resposta:
    ```json
    [
        {
            "Id": 1,
            "Produto": "VINHO DE MESA",
            "Dados": [
            {
                "Ano": 1970,
                "Valor": 217208604
            },
            {
                "Ano": 1971,
                "Valor": 154264651
            },
            ...
            ]
        }
    ]
    ```
    """
    fileProducao = FileProducao(**dadosProducao)
    listaRetornoProducaoCSV = fileProducao.get_list_by_csv()
    print(listaRetornoProducaoCSV[1])
    return {'Data:':listaRetornoProducaoCSV[1]}

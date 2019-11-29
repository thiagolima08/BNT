import data
import os

SQL_FILE_PATH = './data.sql'

def create_sql_estado(estado):
    uf = estado["uf"]
    nome = estado["nome"]
    return f"INSERT INTO estado (uf, nome) VALUES ('{clean_for_sql(uf)}', '{clean_for_sql(nome)}');"

def create_sql_cidade(cidade):
    idCidade = cidade["idCidade"]
    nome = cidade["nome"]
    uf = cidade["uf"]
    return f"INSERT INTO cidade (idCidade, nome, uf) VALUES ('{clean_for_sql(idCidade)}', '{clean_for_sql(nome)}', '{clean_for_sql(uf)}');"

def create_sql_tipo(tipo):
    idTipo = tipo["idTipo"]
    descricao = tipo["descricao"]
    return f"INSERT INTO tipo (idTipo, descricao) VALUES ({clean_for_sql(idTipo)}, '{clean_for_sql(descricao)}');"

def create_sql_marca(marca):
    idMarca = marca["idMarca"]
    nome = marca["nome"]
    origem = marca["origem"]
    return f"INSERT INTO marca (idMarca, nome, origem) VALUES ({clean_for_sql(idMarca)}, '{clean_for_sql(nome)}', '{clean_for_sql(origem)}');"

def create_sql_modelo(modelo):
    idModelo = modelo["idModelo"]
    denominacao = modelo["denominacao"]
    idMarca = modelo["idMarca"]
    idTipo = modelo["idTipo"]
    return f"INSERT INTO modelo (idModelo, denominacao, idMarca, idTipo) VALUES ({clean_for_sql(idModelo)}, '{clean_for_sql(denominacao)}', {clean_for_sql(idMarca)}, {clean_for_sql(idTipo)});"


def create_sql_categoriaCNH(categoriaCNH):
    idCategoriaCNH = categoriaCNH["idCategoriaCNH"]
    descricao = categoriaCNH["descricao"]
    return f"INSERT INTO categoria_cnh (idCategoriaCNH, descricao) VALUES ('{clean_for_sql(idCategoriaCNH)}', '{clean_for_sql(descricao)}');"

def create_sql_condutor(proprietario):
    idCadastro = proprietario["idCadastro"]
    cpf = proprietario["cpf"]
    nome = proprietario["nome"]
    dataNasc = proprietario["dataNasc"]
    idCategoriaCNH = proprietario["idCategoriaCNH"]
    endereco = proprietario["endereco"]
    bairro = proprietario["bairro"]
    idCidade = proprietario["idCidade"]
    situacaoCNH = proprietario["situacaoCNH"]
    
    return f"INSERT INTO condutor (idCadastro, cpf, nome, dataNasc, idCategoriaCNH, endereco, bairro, idCidade, situacaoCNH) VALUES ({clean_for_sql(idCadastro)}, '{clean_for_sql(cpf)}', '{clean_for_sql(nome)}', '{clean_for_sql(dataNasc)}', '{clean_for_sql(idCategoriaCNH)}', '{clean_for_sql(endereco)}', '{clean_for_sql(bairro)}', '{clean_for_sql(idCidade)}', '{clean_for_sql(situacaoCNH)}');"

def create_sql_especie(especie):
    idEspecie = especie["idEspecie"]
    descricao = especie["descricao"]
    return f"INSERT INTO especie (idEspecie, descricao) VALUES ({clean_for_sql(idEspecie)}, '{clean_for_sql(descricao)}');"

def create_sql_categoriaVeiculo(categoriaVeiculo):
    idCategoria = categoriaVeiculo["idCategoria"]
    descricao = categoriaVeiculo["descricao"]
    idEspecie = categoriaVeiculo["idEspecie"]
    return f"INSERT INTO categoria_veiculo (idCategoria, descricao, idEspecie) VALUES ({clean_for_sql(idCategoria)}, '{clean_for_sql(descricao)}', {clean_for_sql(idEspecie)});"

def create_sql_veiculo(categoriaVeiculo):
    placa = categoriaVeiculo["placa"]
    ano = categoriaVeiculo["ano"]
    idCategoria = categoriaVeiculo["idCategoria"]
    idProprietario = categoriaVeiculo["idProprietario"]
    idModelo = categoriaVeiculo["idModelo"]
    idCidade = categoriaVeiculo["idCidade"]
    dataCompra = categoriaVeiculo["dataCompra"]
    dataAquisicao = categoriaVeiculo["dataAquisicao"]
    valor = categoriaVeiculo["valor"]
    situacao = categoriaVeiculo["situacao"]
    return f"INSERT INTO veiculo (placa, ano, idCategoria, idProprietario, idModelo, idCidade, dataCompra, dataAquisicao, valor, situacao) VALUES ('{clean_for_sql(placa)}', {clean_for_sql(ano)}, {clean_for_sql(idCategoria)}, {clean_for_sql(idProprietario)}, {clean_for_sql(idModelo)}, '{clean_for_sql(idCidade)}', '{clean_for_sql(dataCompra)}', '{clean_for_sql(dataAquisicao)}', '{clean_for_sql(valor)}', '{clean_for_sql(situacao)}');"

def create_sql_licenciamento(licenciamento):
    ano = licenciamento["ano"]
    renavam = licenciamento["renavam"]
    dataVenc = licenciamento["dataVenc"]
    pago = licenciamento["pago"]

    return f"INSERT INTO licenciamento (ano, renavam, dataVenc, pago) VALUES ({clean_for_sql(ano)}, '{clean_for_sql(renavam)}', '{clean_for_sql(dataVenc)}', '{clean_for_sql(pago)}');"

def create_sql_transferencia(transferencia):
    idHistorico = transferencia["idHistorico"]
    renavam = transferencia["renavam"]
    idProprietario = transferencia["idProprietario"]
    dataCompra = transferencia["dataCompra"]
    dataVenda = transferencia["dataVenda"]

    return f"INSERT INTO transferencia (idHistorico, renavam, idProprietario, dataCompra, dataVenda) VALUES ({clean_for_sql(idHistorico)}, '{clean_for_sql(renavam)}', {clean_for_sql(idProprietario)}, '{clean_for_sql(dataCompra)}', '{clean_for_sql(dataVenda)}');"

def create_sql_infracoes(infracao):
    idInfracao = infracao["idInfracao"]
    descricao = infracao["descricao"]
    valor = infracao["valor"]
    pontos = infracao["pontos"]
    return f"INSERT INTO infracao (idInfracao,descricao,valor,pontos) VALUES ({clean_for_sql(idInfracao)}, '{clean_for_sql(descricao)}', {clean_for_sql(valor)}, {clean_for_sql(pontos)});"

def create_sql_multas(multa):
    idMulta = multa["idMulta"]
    renavam = multa["renavam"]
    idInfracao = multa["idInfracao"]
    idCondutor = multa["idCondutor"]
    dataInfracao = multa["dataInfracao"]
    dataVencimento = multa["dataVencimento"]
    dataPagamento = multa["dataPagamento"]
    valor = multa["valor"]
    juros = multa["juros"]
    valorFinal = multa["valorFinal"]
    pago = multa["pago"]

    return f"INSERT INTO multa (idMulta,renavam,idInfracao,idCondutor,dataInfracao,dataVencimento,dataPagamento,valor,juros,valorFinal,pago) VALUES ({clean_for_sql(idMulta)}, '{clean_for_sql(renavam)}', {clean_for_sql(idInfracao)}, {clean_for_sql(idCondutor)}, '{clean_for_sql(dataInfracao)}', '{clean_for_sql(dataVencimento)}', '{clean_for_sql(dataPagamento)}', {clean_for_sql(valor)}, {clean_for_sql(juros)}, {clean_for_sql(valorFinal)}, '{clean_for_sql(pago)}');"

def output(saida):
    with open(SQL_FILE_PATH, "a") as sql_file:
        sql_file.write(saida + "\r\n")

def clean_for_sql(value):
    return str(value).replace("'", "")

if __name__ == "__main__":
    if os.path.exists(SQL_FILE_PATH):
        os.remove(SQL_FILE_PATH)

    for key in data.ESTADOS:
        output(create_sql_estado(data.ESTADOS[key]))
    
    for key in data.CIDADES:
        output(create_sql_cidade(data.CIDADES[key]))
    
    for key in data.TIPOS:
        output(create_sql_tipo(data.TIPOS[key]))
    
    for key in data.MARCAS:
        output(create_sql_marca(data.MARCAS[key]))

    for key in data.MODELOS:
        output(create_sql_modelo(data.MODELOS[key]))
    
    for key in data.CATEGORIAS_CNH:
        output(create_sql_categoriaCNH(data.CATEGORIAS_CNH[key]))

    for key in data.CONDUTORES:
        output(create_sql_condutor(data.CONDUTORES[key]))

    for key in data.ESPECIES:
        output(create_sql_especie(data.ESPECIES[key]))
    
    for key in data.CATEGORIAS_VEICULO:
        output(create_sql_categoriaVeiculo(data.CATEGORIAS_VEICULO[key]))
    
    for key in data.VEICULOS:
        output(create_sql_veiculo(data.VEICULOS[key]))
    
    for key in data.LICENCIAMENTOS:
        output(create_sql_licenciamento(data.LICENCIAMENTOS[key]))
    
    for key in data.TRANSFERENCIAS:
        output(create_sql_transferencia(data.TRANSFERENCIAS[key]))
    
    for key in data.INFRACOES:
        output(create_sql_infracoes(data.INFRACOES[key]))
    
    for key in data.MULTAS:
        output(create_sql_multas(data.MULTAS[key]))
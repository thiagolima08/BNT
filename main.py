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
    return f"INSERT INTO especie (idCategoria, descricao, idEspecie) VALUES ({clean_for_sql(idCategoria)}, '{clean_for_sql(descricao)}', {clean_for_sql(idEspecie)});"


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
import data

def create_sql_estado(estado):
    uf = estado["uf"]
    nome = estado["nome"]
    return f"INSERT INTO estado (uf, nome) VALUES ('{uf}', '{nome}');"

def create_sql_cidade(cidade):
    idCidade = cidade["idCidade"]
    nome = cidade["nome"]
    uf = cidade["uf"]
    return f"INSERT INTO cidade (idCidade, nome, uf) VALUES ('{idCidade}', '{nome}', '{uf}');"

def create_sql_tipo(tipo):
    idTipo = tipo["idTipo"]
    descricao = tipo["descricao"]
    return f"INSERT INTO tipo (idTipo, descricao) VALUES ({idTipo}, '{descricao}');"

def create_sql_marca(marca):
    idMarca = marca["idMarca"]
    nome = marca["nome"]
    origem = marca["origem"]
    return f"INSERT INTO marca (idMarca, nome, origem) VALUES ({idMarca}, '{nome}', '{origem}');"

def create_sql_modelo(modelo):
    idModelo = modelo["idModelo"]
    denominacao = modelo["denominacao"]
    idMarca = modelo["idMarca"]
    idTipo = modelo["idTipo"]
    return f"INSERT INTO modelo (idModelo, denominacao, idMarca, idTipo) VALUES ({idModelo}, '{denominacao}', {idMarca}, {idTipo});"

def output(saida):
    print(saida)

if __name__ == "__main__":
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

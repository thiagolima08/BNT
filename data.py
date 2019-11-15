# Dados de marca e modelos:
# https://www.luiztools.com.br/post/base-de-dados-com-todas-as-marcas-e-modelos-de-veiculos/

import csv
from faker import Faker
from random import randint, choice
from datetime import date

import config

fake = Faker('pt_BR')

def criar_sigla_cidade(nome):
    letras_maisculas = [x for x in nome if x.isupper()]

    if len(letras_maisculas) >= 3:
        return "".join(letras_maisculas[0:3])
    
    letra_aleatoria = _pegar_letra_aleatoria(nome)
    
    if len(letras_maisculas) == 2:
        return letras_maisculas[0] + letra_aleatoria.upper() + letras_maisculas[1]
    
    return (nome[0] + nletra_aleatoria + nome[len(nome) - 1]).upper()

def _pegar_letra_aleatoria(texto):
    texto = [x for x in texto if x.isalpha() and x.isascii()]
    return texto[randint(0, len(texto)-1)]

def placaToRenavam (placa):
    renavam = str(ord(placa[0])) + str(ord(placa[1])) + str(ord(placa[2]))
    renavam += placa[3:]

    numeros_validador = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3]
    acumulador = 0
    for i in range(10):
        acumulador += int(renavam[9-i]) * numeros_validador[i]
    acumulador *= 10
    
    renavam += str(acumulador % 11)
    return renavam

ESTADOS = {
    "AC": {"uf": "AC", "nome": "Acre"},
    "AL": {"uf": "AL", "nome": "Alagoas"},
    "AM": {"uf": "AM", "nome": "Amazonas"},
    "AP": {"uf": "AP", "nome": "Amapá"},
    "BA": {"uf": "BA", "nome": "Bahia"},
    "CE": {"uf": "CE", "nome": "Ceará"},
    "DF": {"uf": "DF", "nome": "Distrito Federal"},
    "ES": {"uf": "ES", "nome": "Espírito Santo"},
    "GO": {"uf": "GO", "nome": "Goiás"},
    "MA": {"uf": "MA", "nome": "Maranhão"},
    "MG": {"uf": "MG", "nome": "Minas Gerais"},
    "MS": {"uf": "MS", "nome": "Mato Grosso do Sul"},
    "MT": {"uf": "MT", "nome": "Mato Grosso"},
    "PA": {"uf": "PA", "nome": "Pará"},
    "PB": {"uf": "PB", "nome": "Paraíba"},
    "PE": {"uf": "PE", "nome": "Pernambuco"},
    "PI": {"uf": "PI", "nome": "Piauí"},
    "PR": {"uf": "PR", "nome": "Paraná"},
    "RJ": {"uf": "RJ", "nome": "Rio de Janeiro"},
    "RN": {"uf": "RN", "nome": "Rio Grande do Norte"},
    "RO": {"uf": "RO", "nome": "Rondônia"},
    "RR": {"uf": "RR", "nome": "Roraima"},
    "RS": {"uf": "RS", "nome": "Rio Grande do Sul"},
    "SC": {"uf": "SC", "nome": "Santa Catarina"},
    "SE": {"uf": "SE", "nome": "Sergipe"},
    "SP": {"uf": "SP", "nome": "São Paulo"},
    "TO": {"uf": "TO", "nome": "Tocantins"}
}

CIDADES = {}

for estado in ESTADOS:
    contador = 0
    quantidade_cidade = randint(config.CIDADES_POR_ESTADO_MIN, config.CIDADES_POR_ESTADO_MAX)
    while contador <= quantidade_cidade:
        cidade_nome = fake.city() + " " + fake.city_suffix()
        if cidade_nome[0].islower():
            cidade_nome = cidade_nome[cidade_nome.index(" ") + 1:]
        cidade_sigla = criar_sigla_cidade(cidade_nome)

        if not cidade_sigla in CIDADES:
            cidade = {
                "idCidade": cidade_sigla,
                "nome": cidade_nome,
                "uf": ESTADOS[estado]["uf"]
            }
            CIDADES[cidade_sigla] = cidade
            contador += 1

BAIRROS = {}
# gerando bairros para usar em veículos e proprietários
for cidade in CIDADES:
    contador = 0
    quantidade_bairro = randint(config.BAIRROS_POR_CIDADE_MIN, config.BAIRROS_POR_CIDADE_MAX)
    while contador <= quantidade_bairro:
        bairro_nome = fake.bairro()
        bairro_hash = CIDADES[cidade]["idCidade"] + " - " + bairro_nome

        if not bairro_hash in BAIRROS:
            bairro = {
                "nome": bairro_nome,
                "idCidade": CIDADES[cidade]["idCidade"]
            }
            BAIRROS[bairro_hash] = bairro
            contador += 1

TIPOS = {
    "1": {"idTipo": '1', "descricao": "automóvel"},
    "2": {"idTipo": '2', "descricao": "motocicleta"},
    "3": {"idTipo": '3', "descricao": "caminhão"}
}

MARCAS = {}

with open('./csv/marcas-automovel.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    rows = [x for x in rowreader][1:]
    for row in rows:
        marca_idMarca = row[0]
        marca_nome = row[1]
        marca_origem = fake.country()
        MARCAS[marca_idMarca] = {
            "idMarca": marca_idMarca,
            "nome": marca_nome,
            "origem": marca_origem
        }

with open('./csv/marcas-motocicleta.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    rows = [x for x in rowreader][1:]
    for row in rows:
        marca_idMarca = row[0]
        marca_nome = row[1]
        marca_origem = fake.country()
        MARCAS[marca_idMarca] = {
            "idMarca": marca_idMarca,
            "nome": marca_nome,
            "origem": marca_origem
        }

with open('./csv/marcas-caminhao.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    rows = [x for x in rowreader][1:]
    for row in rows:
        marca_idMarca = row[0]
        marca_nome = row[1]
        marca_origem = fake.country()
        MARCAS[marca_idMarca] = {
            "idMarca": marca_idMarca,
            "nome": marca_nome,
            "origem": marca_origem
        }

MODELOS = {}

with open('./csv/modelos-automovel.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    rows = [x for x in rowreader][1:]
    for row in rows:
        modelo_idModelo = row[0]
        modelo_denominacao = row[2]
        modelo_idMarca = row[1]
        modelo_idTipo = "1"
        if modelo_idMarca in MARCAS:
            MODELOS[modelo_idModelo] = {
                "idModelo": modelo_idModelo,
                "denominacao": modelo_denominacao,
                "idMarca": modelo_idMarca,
                "idTipo": modelo_idTipo
            }

with open('./csv/modelos-motocicleta.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    rows = [x for x in rowreader][1:]
    for row in rows:
        modelo_idModelo = row[0]
        modelo_denominacao = row[2]
        modelo_idMarca = row[1]
        modelo_idTipo = "2"
        if modelo_idMarca in MARCAS:
            MODELOS[modelo_idModelo] = {
                "idModelo": modelo_idModelo,
                "denominacao": modelo_denominacao,
                "idMarca": modelo_idMarca,
                "idTipo": modelo_idTipo
            }

with open('./csv/modelos-caminhao.csv', newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    rows = [x for x in rowreader][1:]
    for row in rows:
        modelo_idModelo = row[0]
        modelo_denominacao = row[2]
        modelo_idMarca = row[1]
        modelo_idTipo = "3"
        if modelo_idMarca in MARCAS:
            MODELOS[modelo_idModelo] = {
                "idModelo": modelo_idModelo,
                "denominacao": modelo_denominacao,
                "idMarca": modelo_idMarca,
                "idTipo": modelo_idTipo
            }

CATEGORIAS_CNH = {
    "ACC": {"idCategoriaCNH": "ACC", "descricao": "Habilita pessoas conduzam veículos de duas rodas com até 50 cm3 de cilindrada, as conhecidas \"cinquentinhas\"."},
    "A": {"idCategoriaCNH": "A", "descricao": "Habilita a conduzir veículos de duas ou três rodas, com mais que 50 de cilindrada. Além disso, também é possível conduzir os ciclomotores da categoria ACC."},
    "B": {"idCategoriaCNH": "B", "descricao": "Habilita o condutor a conduzir veículos de quatro rodas com até 3,5 toneladas de peso bruto total e capacidade para até oito passageiros, além do motorista (nove ocupantes no total). Quadriciclos estão inclusos nesta classe."},
    "C": {"idCategoriaCNH": "C", "descricao": "Habilita o condutor a dirigir todos os tipos de automóveis da categoria B, e também os veículos de carga, não articulados, com mais de 3,5 toneladas de peso bruto total. São exemplos os caminhões, tratores, máquinas agrícolas e de movimentação de carga."},
    "D": {"idCategoriaCNH": "D", "descricao": "Habilita o condutor a dirigir veículos para o transporte de passageiros que acomodem mais de 8 passageiros. Aqui, entram os ônibus, micro-ônibus e vans. Com ela, o condutor também pode comandar todos os veículos inclusos nos tipos de CNH B e C."},
    "E": {"idCategoriaCNH": "E", "descricao": "Todos os veículos inclusos nos tipos de CNH B, C e D. Além disso, ele também pode dirigir veículos com unidades acopladas que excedam 6 toneladas. Aqui estão as carretas e caminhões com reboques e semirreboques articulados. Por fim, é necessário ter a carteira E para conduzir carros puxando trailers."}
}

CONDUTORES = {}
cpfs = set()
bairros_keys = [x for x in BAIRROS.keys()]
contador = 1
quantidade_condutores = randint(config.CONDUTORES_MIN, config.CONDUTORES_MAX)
while contador <= quantidade_condutores:

    cpf = "".join([x for x in fake.cpf() if x.isnumeric()])
    while cpf in cpfs:
        cpf = "".join([x for x in fake.cpf() if x.isnumeric()])
    bairro_hash = choice(bairros_keys)
    bairro = BAIRROS[bairro_hash]

    CONDUTORES[str(contador)] = {
        "idCadastro": str(contador),
        "cpf": cpf,
        "nome": fake.name_female() if randint(1, 2) % 2 == 0 else fake.name_male(),
        "dataNasc": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "idCategoriaCNH": "ABCDE"[randint(0, 4)],
        "endereco": fake.street_address(),
        "bairro": bairro["nome"],
        "_bairro_hash": bairro_hash,
        "idCidade": bairro["idCidade"],
        "situacaoCNH": "R"
    }
    contador += 1

ESPECIES = {
    "1": {"idEspecie": '1', "descricao": "de passageiros"},
    "2": {"idEspecie": '2', "descricao": "de carga"},
    "3": {"idEspecie": '3', "descricao": "misto"},
    "4": {"idEspecie": '4', "descricao": "de competição"},
    "5": {"idEspecie": '5', "descricao": "de tração"},
    "6": {"idEspecie": '6', "descricao": "especial"},
    "7": {"idEspecie": '7', "descricao": "de coleção"}
}


CATEGORIAS_VEICULO = {}
contador = 1
for key in ESPECIES:
    categorias = ['Particular', 'Oficial', 'Aprendizagem', 'Aluguel', 'Representação Diplomática']
    for categoria in categorias:
        CATEGORIAS_VEICULO[str(contador)] = {
            "idCategoria": str(contador),
            "descricao": categoria,
            "idEspecie": key
        }
        contador += 1

VEICULOS = {}
placas = set()
condurores_keys = [x for x in CONDUTORES.keys()]
modelos_keys = [x for x in MODELOS.keys()]
categoria_veiculo_keys = [x for x in CATEGORIAS_VEICULO.keys()]
quantidade_veiculos = randint(config.VEICULOS_MIN, config.VEICULOS_MAX)
for _ in range(1, quantidade_veiculos):
    placa = "".join([x for x in fake.license_plate() if x != '-'])
    while placa in placas:
        placa = "".join([x for x in fake.license_plate() if x != '-'])
        
    bairro = BAIRROS[choice(bairros_keys)]

    renavam = placaToRenavam(placa)

    proprietario = choice(condurores_keys)
    ano = fake.year()
    dataCompra =  fake.date_between_dates(date_start=date(int(ano),1,1), date_end=date(int(ano),12,31))
    VEICULOS[renavam] = {
        "renavam": renavam,
        "placa": placa,
        "ano": ano,
        "idCategoria": choice(categoria_veiculo_keys),
        "idProprietario": proprietario,
        "idModelo": choice(modelos_keys),
        "idCidade": BAIRROS[CONDUTORES[proprietario]["_bairro_hash"]]["idCidade"],
        "dataCompra": dataCompra,
        "dataAquisicao": dataCompra,
        "valor": fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        "situacao": "R"
    }


# Dados de marca e modelos:
# https://www.luiztools.com.br/post/base-de-dados-com-todas-as-marcas-e-modelos-de-veiculos/

import csv
from faker import Faker
from random import randint
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
    "1": {"idTipo": 1, "descricao": "automóvel"},
    "2": {"idTipo": 2, "descricao": "motocicleta"},
    "3": {"idTipo": 3, "descricao": "caminhão"}
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
        MODELOS[modelo_idModelo] = {
            "idModelo": modelo_idModelo,
            "denominacao": modelo_denominacao,
            "idMarca": modelo_idMarca,
            "idTipo": modelo_idTipo
        }

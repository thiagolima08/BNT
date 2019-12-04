# -*- coding: utf-8 -*-
import psycopg2 
from prettytable import PrettyTable

conn = psycopg2.connect("dbname=BNT user=postgres host=localhost")
cur = conn.cursor()   

def situacao_veiculo(renavam):
    cur.execute("SELECT situacao FROM veiculo WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    sit= res[0][0]
    if sit == 'B':
        return 'Bloqueado'
    if sit == 'I':
        return 'Inativo'
    if sit == 'R':
        return 'Regular'

def situacao_cnh(cpf):
    cur.execute("SELECT situacaoCNH FROM condutor WHERE cpf='%s';"%cpf)
    res = cur.fetchall()  
    sit= res[0][0]
    if sit == 'S':
        return 'Suspensa'
    if sit == 'R':
        return 'Regular'

def situacao_licenciamento(renavam):
    cur.execute("SELECT pago FROM licenciamento WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    sit= res[0][0]
    if sit == 'S':
        return 'Sim'
    if sit == 'N':
        return 'Não'

def situacao_multa(renavam):
    cur.execute("SELECT pago FROM multa WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    sit= res[0][0]
    if sit == 'S':
        return 'Sim'
    if sit == 'N':
        return 'Não'

def info_veiculo(renavam):
    cur.execute("SELECT mo.denominacao, ma.nome, ti.descricao, vei.placa, vei.ano FROM modelo mo JOIN marca ma ON mo.idMarca=ma.idMarca JOIN tipo ti ON mo.idTipo=ti.idTipo JOIN veiculo vei ON vei.idModelo=mo.idModelo WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    mod = res[0][0]
    mar = res[0][1]
    tip = res[0][2]
    pla = res[0][3]
    ano = res[0][4]
    return "\nPlaca: "+pla+"\nModelo: "+mod+"\nAno: "+str(ano)+"\nMarca: "+mar+"\nTipo: "+tip+"\nSituação: "+situacao_veiculo(renavam)+"\n"

def consulta_proprietario(renavam):
    cur.execute("SELECT co.nome FROM veiculo ve JOIN condutor co ON ve.idProprietario=co.idCadastro WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    nome= res[0][0]
    return "\nProprietário do veículo: "+nome+"\n"

def historico_veiculo(renavam):
    cur.execute("SELECT historico_transacao('%s');"%renavam)
    res = cur.fetchall()
    rp=[]
    for r in range(len(res)):
        rp += res[r]
    t = PrettyTable(["Modelo","Marca","Ano","Proprietário","Data de Compra","Data de Venda"])
    for j in range(len(rp)):
        tab = rp[j].split(',')
        t.add_row(tab[1:])       
    return t

def info_condutor(cpf):
    cur.execute("SELECT nome,dataNasc,endereco,idCategoriaCNH FROM condutor WHERE cpf='%s';"%cpf)
    res = cur.fetchall()  
    nome = res[0][0]
    data = res[0][1]
    data_form = "{:%d/%m/%Y}".format(data)
    endereco = res[0][2]
    cat_cnh = res[0][3]
    return "\nNome: "+nome+"\nData de Nascimento: "+data_form+"\nEndereço: "+endereco+"\nCategoria de CNH: "+cat_cnh+"\nSituação: "+situacao_cnh(cpf)+"\n"

def info_lincenciamento(renavam):
    cur.execute("SELECT ano,dataVenc from licenciamento WHERE renavam = '%s';"%renavam)
    res = cur.fetchall()
    ano = res[0][0]
    data = res[0][1]
    data_form = "{:%d/%m/%Y}".format(data)
    return "\nAno: "+str(ano)+"\nData de Vencimento: "+data_form+"\nPago: "+situacao_licenciamento(renavam)+"\n"

def consulta_multa(renavam):
    cur.execute("SELECT co.nome,inf.descricao,inf.valor,inf.pontos,mu.dataVencimento FROM multa mu JOIN infracao inf ON mu.idInfracao = inf.idInfracao JOIN condutor co ON co.idCadastro = mu.idCondutor WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    if res==[]:
         return "\n-> O veículo não possui multas\n"
    else:
        rp=[]
        t = PrettyTable(["Condutor","Infração","Valor","Pontos","Data de Vencimento"])
        for i in range(len(res)):
            rp.append(res[i])
        for r in rp:
            t.add_row(r)       
        return t
    
def condutores_pontos():
    cur.execute("SELECT *  FROM condutor_com_pontos;")
    res = cur.fetchall()  
    rp=[]
    t = PrettyTable(["idCadastro","Nome do condutor","Categoria","Ano da infração","Pontos"])
    for i in range(len(res)):
        rp.append(res[i])
    for r in rp:
        t.add_row(r)       
    return t

def veiculo_proprietario():
    cur.execute("SELECT *  FROM veiculos_proprietarios;")
    res = cur.fetchall()  
    rp=[]
    t = PrettyTable(["Renavam","Placa","Proprietário","Modelo","Marca","Cidade","Estado","Tipo"])
    for i in range(len(res)):
        rp.append(res[i])
    for r in rp:
        t.add_row(r)       
    return t

def infracoes_multas():
    cur.execute("SELECT *  FROM num_infracoes_e_valores_multas ORDER BY 1,2")
    res = cur.fetchall()  
    rp=[]
    t = PrettyTable(["Ano","Mês","Quantidade de infrações","Valor total de multas"])
    for i in range(len(res)):
        rp.append(res[i])
    for r in rp:
        t.add_row(r)       
    return t

def imprimir_menu():
    print("-------------------------")
    print("- MENU -")
    print("-------------------------")
    print("(1) Informações do veículo")
    print("(2) Consultar proprietário do veículo")
    print("(3) Histórico de transferência do veículo")
    print("(4) Informações do Condutor")
    print("(5) Informações do licenciamento")
    print("(6) Consultar multas")
    print("(7) Menu de relatórios")
    print("(0) Sair do programa")

def menu_relatorios():
    print("-------------------------")
    print("- RELATÓRIOS -")
    print("-------------------------")
    print("(1) Pontos dos condutores")
    print("(2) Relação de Veículos e Proprietários")
    print("(3) Número de infrações e valores das multas")
    print("(4) Para voltar ao menu inicial")
    print("(0) Sair do programa")

#Entradas (testes):
#Renavam = 86727075753
#cpf = 45391680298

while True:
    imprimir_menu()
    menu_selected = input("Escolha uma opção: ")
    if menu_selected == "1":
        r = input("Digite o renavam: ")
        print(info_veiculo(r))
    if menu_selected == "2":
        r = input("Digite o renavam: ")
        print(consulta_proprietario(r)) 
    if menu_selected == "3":
        r = input("Digite o renavam: ")
        print(historico_veiculo(r))
    if menu_selected == "4":
        c = input("Digite o cpf: ")
        print(info_condutor(c))
    if menu_selected == "5":
        r = input("Digite o renavam: ")
        print(info_lincenciamento(r))
    if menu_selected == "6":
        r = input("Digite o renavam: ")
        print(consulta_multa(r))
    if menu_selected == "7":
        menu_relatorios()
        menu_selected = input("Escolha uma opção: ")
        if menu_selected == "1":
            print(condutores_pontos())
        if menu_selected == "2":
            print(veiculo_proprietario())
        if menu_selected == "3":
            print(infracoes_multas()) 
        if menu_selected == "4":
            continue
        if menu_selected == "0":
            break
    if menu_selected == "0":
        break

cur.close()
conn.close()
exit()
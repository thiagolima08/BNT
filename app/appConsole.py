# -*- coding: utf-8 -*-
import psycopg2 

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
    return "Placa: "+pla+"\nModelo: "+mod+"\nAno: "+ano+"\nMarca: "+mar+"\nTipo: "+tip+"\nSituação: "+situacao_veiculo(renavam)

def consulta_proprietario(renavam):
    cur.execute("SELECT co.nome FROM veiculo ve JOIN condutor co ON ve.idProprietario=co.idCadastro WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    nome= res[0][0]
    return "Proprietário do veículo: "+nome

def historico_veiculo(renavam):
    cur.execute("SELECT historico_transacao('%s');"%renavam)
    res = cur.fetchall()
    return res[0][0]

def info_condutor(cpf):
    cur.execute("SELECT nome,dataNasc,endereco,idCategoriaCNH FROM condutor WHERE cpf='%s';"%cpf)
    res = cur.fetchall()  
    nome = res[0][0]
    data = res[0][1]
    data_form = "{:%d/%m/%Y}".format(data)
    endereco = res[0][2]
    cat_cnh = res[0][3]
    print()
    return "Nome: "+nome+"\nData de Nascimento: "+data_form+"\nEndereço: "+endereco+"\nCategoria de CNH: "+cat_cnh+"\nSituação: "+situacao_cnh(cpf)

def info_lincenciamento(renavam):
    cur.execute("SELECT ano,dataVenc from licenciamento WHERE renavam = '%s';"%renavam)
    res = cur.fetchall()
    ano = res[0][0]
    data = res[0][1]
    data_form = "{:%d/%m/%Y}".format(data)
    return "Ano: "+str(ano)+"\nData de Vencimento: "+data_form+"\nPago: "+situacao_licenciamento(renavam)

def consulta_multa(renavam):
    cur.execute("SELECT co.nome,inf.descricao,inf.valor,inf.pontos,mu.dataVencimento FROM multa mu JOIN infracao inf ON mu.idInfracao = inf.idInfracao JOIN condutor co ON co.idCadastro = mu.idCondutor WHERE renavam='%s';"%renavam)
    res = cur.fetchall()  
    if res==[]:
         return "O veículo não possui multas"
    else:
        nome = res[0][0]
        tipo_infr = res[0][1]
        valor = res[0][2]
        pontos = res[0][3]
        data_venc = res[0][4]
        data_venc_form = "{:%d/%m/%Y}".format(data_venc)
        valor_form = '%.2f'%valor
        return "Condutor: "+nome+"\nInfração: "+tipo_infr+"\nValor: "+valor_form+"\nPontuação da Infração: "+str(pontos)+"\nData de Vencimento: "+data_venc_form+"\nPago: "+situacao_multa(renavam)

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
    print("(7) Sair do programa")

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
        break

cur.close()
conn.close()
exit()
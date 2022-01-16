from terminal_system.classes import Cliente,Consultor
from time import sleep

contratos={}
clientes = {}
consultores = {}

#Bloco de funções do Menu principal
def criar_consultor(): #não adiciona no dic e nem cria consultor
    username = input("Username\n")
    password = input("Password\n")
    
    print("Consultor adicionado ao sistema!")
    return None

def criar_cliente(): #não adiciona no dic e nem cria cliente
    username = input("Username\n")
    password = input("Password\n")
    
    print("Consultor adicionado ao sistema!")
    return None
          
def criar_Contrato():
    title = input("Title\n")
    description = input("Description\n")
    end_period = input("End Period\n")

    if len(clientes)==0 or len(consultores)==0:
        print("Não há clientes e/ou consultores cadastrados.")
        return None
    else:
        cliente = clientes.keys(input('Id do cliente:\n'))
        consultor = consultores.keys(input('Id do consultor:\n'))
    
    ###erro de importação!!
    contrato = Contrato(title,end_period,description=description,associates=f'{cliente}/{consultor}') ### como está falado no classes.py, associates deveria ser uma lista
    contratos[f'{contrato.id}']=contrato
    print("Consultor adicionado ao sistema!") ### print errado
    return None

from classes import Cliente,Consultor

s=None
contratos={}
clientes = {}
consultores = {}

#Bloco de funções do Menu principal
def post_consultor(): #não adiciona no dic e nem cria consultor
    username = input("Username\n")
    password = input("Password\n")
    print("Consultor adicionado ao sistema!")
    return None

def post_cliente(): #não adiciona no dic e nem cria cliente
    username = input("Username\n")
    password = input("Password\n")
    
    print("Consultor adicionado ao sistema!")
    return None
          
def post_contrato():
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

def conclude_contrato():
    try:contrato = contratos[input("Id do Contrato:\n")]
    except KeyError:
        print("Não existe contrato com esse id")
    contrato.conclude_contract()

def get_consultores():
    print("Consultor Log")
    for consultor in consultores.values():
        consultor.view()
    print("----------------------------")

def get_consultor():
    print("Consultor Log")
    id = int(input("Id do consultor"))
    consultores[id].view()
    print("----------------------------")

def delete_consultor():
    username = input("Username\n")
    password = input("Password\n")
    print("----------------------------")
from classes import *
from comandos import *

def menu():
    while True:
        print("Protótipo Sistema Terminal Rosa's Consultoria, o que deseja?\n",
        "(1)Cadastrar Consultor\n",
        "(2)Cadastrar Cliente\n",
        "(3)Criar Contrato\n",
        "(4)Sair do Sistema\n")
        inp = input()
        if inp == 1:criar_consultor()
        if inp == 2:criar_cliente()
        if inp == 3:criar_Contrato()
        if inp == 4:break
        else:print('Comando Inválido')

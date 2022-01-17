from comandos import *

def menu():
    while True:
        print("Protótipo Sistema Terminal Rosa's Consultoria, o que deseja?\n",
        "(1)Cadastrar Consultor\n",
        "(2)Cadastrar Cliente\n",
        "(3)Criar Contrato\n",
        "(4)Visualizar Consultores\n",
        "(5)Visualizar Consultor\n",
        "(s)Sair do Sistema\n")
        inp = input()
        ### Respostas dos inputs sempre darao erro
        if inp == 1:post_consultor()
        if inp == 2:post_cliente()
        if inp == 3:post_contrato()
        if inp == 4:get_consultores()
        if inp == 5: get_consultor()
        if inp == s:break ### nunca irá dar break, pois s é None
        else:print('Comando Inválido')
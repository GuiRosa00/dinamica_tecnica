from random import seed
import datetime

class Contrato:

    def __init__(self, title:int, end_period:datetime.datetime, description = '',associates=''):
        ### INICIALIZA A CLASSE DOS CONTRATOS DO SISTEMA
        self.title = title
        self.associates = associates
        self.description = descript
        self.id = seed()
        self.created_dt = datetime.datetime.now()
        self.end_period = end_period
        return None
    
    def __review__(self):
        print("Status:",'\n')
        print("Title:",str(title))
        for i in self.associates: ### deveria printar os membros e o id, mas ta printando letras kkkk
            print("Associates:",i)
        print('\n',self.description)
        print('Concluded': self.concluded)
        return None
    
    def conclude_contract(self):
        if self.concluded:
            print("Contrato já concluído")
            return None
        self.concluded = 1
        print("Contrato Concluído!")
        return None
    
    def terminate_contract(self): ### Isso não deveria ser um método pela sua estrutura
        inp = input("Você realmente pretende terminar este contrato?",
        '\n (s)Sim',
        '\n (n)Não')
        if inp.lower() == 'S':
            return 1
        else:
            return 0
        
    def extend_contract(self,end_period:datetime.datetime):
        self.end_period = end_period
        return None

class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.status = 'Blank_User'
        return None
    
    def view(self,user_try,pass_try):
        if self.username == user_try and self.password==pass_try:
            print("Username:",self.username)
            print("Status:", self.status)
        print("Error, invalid user")

class Consultor(User):
    def __init__(self,username,password):
        super.__init__(username,password)
        self.status = 'Consultant'
        self.id = f'C{seed()}'
        self.projects = []
        return None

class Cliente:

    def __init__(self,username,password):
        super.__init__(username,password)
        self.status = 'Client'
        self.id = f'C{seed()}' ## Confusão nos dados
        self.contracts = []
        return None

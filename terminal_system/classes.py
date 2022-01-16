from random import randint
import datetime
import hashlib

class IdGenerator:
    def __init__(self,):
        '''Essa classe serve como uma forma de geração dos ids dos usuários, 
        e não necessita ser avaliada pelos candidatos.'''
        return None
    def generate(self,):
        output_id = ''
        for i in range(10):output_id += str(randint(0,9))
        return output_id

id_generator = IdGenerator()

class Contrato:

    def __init__(self, title, end_period, description = '',associates=''):
        """Essa classe é responsável por inicializar uma instância 
        de um Contrato, dado um certo título, data de termino, descrição, consultor e cliente."""
        ### INICIALIZA A CLASSE DOS CONTRATOS DO SISTEMA
        self.title = int(title) ### title está como int no init, ele deveria ser uma str
        self.associates = associates # está setado como str, mas ele deve se tornar uma lista!
        self.description = descript ## erro de nome
        self.id = f'C{id_generator.generate()}'
        self.created_dt = f'{datetime.datetime.now()}'
        self.end_period = end_period
        self.concluded = 0
        return None

    @staticmethod ### decorator inválido, deveria ser removido ou substituído por @classmethod
    def __review__(self,): ### esse método mágico está incorreto, deveria ser __str__ ou __repr__
        print("Status:",'\n')
        print("Title:",str(title)) ### falta self no title, e não é necessário colocar str()
        for i in self.associates: 
            ### no caso, ele estaria printando cada letra da str,
            #  eles devem perceber esse erro, e por isso transformar em lista
            print("Associates:",i)
        print('\n',self.description)
        print('Concluded':self.concluded)## está com : fora do print e sem ','
        return None
    
    def conclude_contract(self): 
        ### método que poderia ser jogado para fora da classe 
        #(não seria essencial para avaliação), já que é de lógica extremamente simples
        if self.concluded:
            print("Contrato já concluído")
            return None
        self.concluded = 1
        print("Contrato Concluído!")
        return None
    
    def terminate_contract(self): ### Isso não deveria ser um método.
        inp = input("Você realmente pretende terminar este contrato?",
        '\n (s)Sim',
        '\n (n)Não')
        if inp.lower() == 'S':
            return 1
        else:
            return 0

class User:

    def init(self,username,password): ## sem o __
        '''Essa classe serve como um modelo base para a interação tanto para os Consultores quanto para os Clientes que
        utilizaram o terminal.'''
        self.username = username
        self.password = password
        self.status = 'Blank_User'
        self.id = f'U{id_generator.generate()}'
        return None
    
    def view(self,user_try,pass_try):
        if self.username == user_try and self.password==pass_try:
            print("Username:",self.username)
            print("Status:", self.status)
            print("Id:", self.id)
            return None
        print("Error, invalid user")

class Consultor(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.status = 'Consultant'
        self.id = f'C{id_generator.generate()}'
        self.projects = []
        return None

class Cliente:
    def __init__(self,username,password):
        super().__init__(username,password) ### Existe um super.__init__, mas não tem hierarquia definida
        self.status = 'Client'
        ### Percebe-se que tanto o consultor como o Cliente e o contrato possuem um 'C...', 
        # isso deveria ser resolvido por questões estruturais de confusão, mas seria algo mais supérfulo
        self.id = f'C{id_generator.generate()}'
        self.contracts = []
        return None

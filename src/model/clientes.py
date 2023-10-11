class Cliente:
    def __init__(self,
                 CPF:str=None,
                 idCliente:str=None, 
                 nome:str=None,
                 email:str=None,
                 telefone:int=None,
                 endereco:str=None,
                ):
        self.set_CPF(CPF)
        self.set_idCliente(idCliente)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_endereco(endereco)

    #Getters  
    def get_CPF(self) -> str:
        return self.CPF
    
    def get_idCliente(self) -> str:
        return self.idCliente

    def get_nome(self) -> str:
        return self.nome
    
    def get_email(self) -> str:
        return self.email
    
    def get_telefone(self) -> int:
        return self.telefone

    def get_endereco(self) -> str:
        return self.endereco
    
#Setters

    def set_idCliente(self, idCliente:str):
        self.idCliente = idCliente

    def set_nome(self, nome:str):
        self.nome = nome

    def set_CPF(self, CPF:str):
        self.CPF = CPF

    def set_email(self, email:str):
        self.email = email

    def set_telefone(self, telefone:int):
        self.telefone = telefone

    def set_endereco(self, endereco:str):
        self.endereco = endereco    

#ToString
    def to_string(self) -> str:
        return f"CPF: {self.get_CPF()} | Nome: {self.get_nome()}| {self.get_email}| {self.get_endereco}|{self.get_telefone}"
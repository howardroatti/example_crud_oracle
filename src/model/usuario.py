class Usuario:
    def __init__(self, id_usuario:int=None, nome:str=None, email:str=None, telefone:str=None):
        self.set_id_usuario(id_usuario)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)

    #Setters

    def set_id_usuario(self, id_usuario:int):
        self.id_usuario = id_usuario

    def set_nome(self, nome:str):
        self.nome = nome

    def set_email(self, email:str):
        self.email = email

    def set_telefone(self, telefone:str):
        self.telefone = telefone

    #Getters
    
    def get_id_usuario(self) -> int:
        return self.id_usuario

    def get_nome(self) -> str:
        return self.nome

    def get_email(self) -> str:
        return self.email

    def get_telefone(self) -> str:
        return self.telefone

    def to_string(self) -> str:
        return f"ID: {self.get_id_usuario()} | Nome: {self.get_nome()} | Email: {self.get_email()} | Telefone: {self.get_telefone()}"
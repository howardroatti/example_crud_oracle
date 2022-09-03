class Cliente:
    def __init__(self, 
                 CPF:str=None, 
                 nome:str=None
                ):
        self.set_CPF(CPF)
        self.set_nome(nome)

    def set_CPF(self, CPF:str):
        self.CPF = CPF

    def set_nome(self, nome:str):
        self.nome = nome

    def get_CPF(self) -> str:
        return self.CPF

    def get_nome(self) -> str:
        return self.nome

    def to_string(self) -> str:
        return f"CPF: {self.get_CPF()} | Nome: {self.get_nome()}"
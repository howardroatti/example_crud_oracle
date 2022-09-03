class Produto:
    def __init__(self, 
                 codigo:int=None, 
                 descricao:str=None
                 ):
        self.set_codigo(codigo)
        self.set_descricao(descricao)

    def set_codigo(self, codigo:int):
        self.codigo = codigo

    def set_descricao(self, descricao:str):
        self.descricao = descricao

    def get_codigo(self) -> int:
        return self.codigo

    def get_descricao(self) -> str:
        return self.descricao

    def to_string(self) -> str:
        return f"Codigo: {self.get_codigo()} | Descrição: {self.get_descricao()}"
class Categoria:
    def __init__(self, id_categoria:int=None, nome_categoria:str=None):
        self.set_id_categoria(id_categoria)
        self.set_nome_categoria(nome_categoria)

    def set_id_categoria(self, id_categoria:int):
        self.id_categoria = id_categoria

    def set_nome_categoria(self, nome_categoria:str):
        self.nome_categoria = nome_categoria

    def get_id_categoria(self) -> int:
        return self.id_categoria

    def get_nome_categoria(self) -> str:
        return self.nome_categoria

    def to_string(self) -> str:
        return f"ID Categoria: {self.get_id_categoria()} | Nome Categoria: {self.get_nome_categoria()}"

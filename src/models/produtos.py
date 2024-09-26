from models.categoria import Categoria

class Produto:
    def __init__(self, id_produto:int=None, nome_produto:str=None, preco:float=None, categoria:Categoria=None):
        self.set_id_produto(id_produto)
        self.set_nome_produto(nome_produto)
        self.set_preco(preco)
        self.set_categoria(categoria)

    def set_id_produto(self, id_produto:int):
        self.id_produto = id_produto

    def set_nome_produto(self, nome_produto:str):
        self.nome_produto = nome_produto

    def set_preco(self, preco:float):
        self.preco = preco

    def set_categoria(self, categoria:Categoria):
        self.categoria = categoria

    def get_id_produto(self) -> int:
        return self.id_produto

    def get_nome_produto(self) -> str:
        return self.nome_produto

    def get_preco(self) -> float:
        return self.preco

    def get_categoria(self) -> Categoria:
        return self.categoria

    def to_string(self) -> str:
        return f"ID Produto: {self.get_id_produto()} | Nome Produto: {self.get_nome_produto()} | Preço: {self.get_preco()} | Categoria: {self.get_categoria().get_nome_categoria()}"

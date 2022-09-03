from model.pedidos import Pedido
from model.produtos import Produto

class ItemPedido:
    def __init__(self, 
                 codigo_item:int=None,
                 quantidade:float=None,
                 valor_unitario:float=None,
                 pedido:Pedido=None,
                 produto:Produto=None
                 ):
        self.set_codigo_item(codigo_item)
        self.set_quantidade(quantidade)
        self.set_valor_unitario(valor_unitario)
        self.set_pedido(pedido)
        self.set_produto(produto)

    def set_codigo_item(self, codigo_item:int):
        self.codigo_item = codigo_item

    def set_quantidade(self, quantidade:float):
        self.quantidade = quantidade

    def set_valor_unitario(self, valor_unitario:float):
        self.valor_unitario = valor_unitario
    
    def set_pedido(self, pedido:Pedido):
        self.pedido = pedido

    def set_produto(self, produto:Produto):
        self.produto = produto

    def get_codigo_item(self) -> int:
        return self.codigo_item

    def get_quantidade(self) -> float:
        return self.quantidade

    def get_valor_unitario(self) -> float:
        return self.valor_unitario
    
    def get_pedido(self) -> Pedido:
        return self.pedido

    def get_produto(self) -> Produto:
        return self.produto

    def to_string(self):
        return f"Item: {self.get_codigo_item()} | Quant.: {self.get_quantidade()} | Vlr. Unit.: {self.get_valor_unitario()} | Prod.: {self.get_produto().get_descricao()} | Ped: {self.get_pedido().get_codigo_pedido()}"
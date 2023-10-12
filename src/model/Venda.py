from datetime import date
from model.clientes import Cliente
from model.veiculos import Veiculo

class VendaVeiculo:
    def __init__(self, 
                 idVenda:int=None,
                 valorVenda:float=None,
                 dataVenda:date=None,
                 idVendedor:int=None,
                 Cliente:str=None,
                 Veiculo:str=None
                 ):
        self.set_idVenda(idVenda)
        self.set_valorVenda(valorVenda)
        self.set_dataVenda(dataVenda)
        self.set_idVendedor(idVendedor)
        self.set_cliente(Cliente)
        self.set_veiculos(Veiculo)
#Getters
    def get_idVenda(self) -> int:
        return self.idVenda

    def get_valorVenda(self) -> float:
        return self.valorVenda
    
    def get_dataVenda(self) -> date:
        return self.datavenda

    def get_idVendedor(self) -> int:
        return self.set_idVendedor

    def get_cliente(self) -> Cliente:
        return self.cliente

    def get_veiculos(self) -> Veiculos:
        return self.veiculos

#Setters
    def set_idVenda(self, idVenda: int):
        self.idVenda = idVenda

    def set_valorVenda(self, valorVenda: float):
        self.valorVenda = valorVenda

    def set_dataVenda(self, dataVenda: date):
        self.datavenda(self, dataVenda)

    def set_idVendedor(self, idVendedor: int):
        self.idVendedor(self, idVendedor)

    def set_cliente(self, cliente: Cliente):
        self.cliente = cliente

    def set_veiculos(self, veiculos: Veiculos):
        self.veiculos = veiculos

#ToString
    def to_string(self) -> str:
        return (f"Venda: {self.get_idVenda()} | Valor: {self.get_valorVenda()} | Data: {self.get_dataVenda()} |"
        f" Vendedor: {self.get_idVendedor()} | Cliente: {self.get_cliente().get_cpfCliente()} | Veiculo: {self.get_veiculos().get_idVeiculos()}")

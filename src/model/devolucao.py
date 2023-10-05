from model.emprestimo import Emprestimo

class Devolucao:
    def __init__(self, id_devolucao:int=None, emprestimo:Emprestimo=None, data_devolucao:str=None):
        self.set_id_devolucao(id_devolucao)
        self.set_emprestimo(emprestimo)
        self.set_data_devolucao(data_devolucao)

    #Setters

    def set_id_devolucao(self, id_devolucao:int):
        self.id_devolucao = id_devolucao

    def set_emprestimo(self, emprestimo:Emprestimo):
        self.emprestimo = emprestimo

    def set_data_devolucao(self, data_devolucao:str):
        self.data_devolucao = data_devolucao

    #Getters
    
    def get_id_devolucao(self) -> int:
        return self.id_devolucao

    def get_emprestimo(self) -> Emprestimo:
        return self.emprestimo

    def get_data_devolucao(self) -> str:
        return self.data_devolucao

    def to_string(self) -> str:
        return f"ID: {self.get_id_devolucao()} | Emprestimo ID: {self.get_emprestimo().get_id_emprestimo()} | Data de Devolução: {self.get_data_devolucao()} | Data de Devolução Sugerida: {self.get_emprestimo().get_data_devolucao()}"
    
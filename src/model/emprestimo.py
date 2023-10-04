from model.livro import Livro
from model.usuario import Usuario

class Emprestimo:
    def __init__(self, id_emprestimo:int=None, livro:Livro=None, usuario:Usuario=None, data_emprestimo:str=None, data_devolucao:str=None):
        self.set_id_emprestimo(id_emprestimo)
        self.set_livro(livro)
        self.set_usuario(usuario)
        self.set_data_emprestimo(data_emprestimo)
        self.set_data_devolucao(data_devolucao)

    #Setters

    def set_id_emprestimo(self, id_emprestimo:int):
        self.id_emprestimo = id_emprestimo

    def set_data_emprestimo(self, data_emprestimo:str):
        self.data_emprestimo = data_emprestimo

    def set_data_devolucao(self, data_devolucao:str):
        self.data_devolucao = data_devolucao

    def set_livro(self, livro:Livro):
        self.livro = livro

    def set_usuario(self, usuario:Usuario):
        self.usuario = usuario

    #Getters
    
    def get_id_emprestimo(self) -> int:
        return self.id_emprestimo

    def get_data_emprestimo(self) -> str:
        return self.data_emprestimo

    def get_data_devolucao(self) -> str:
        return self.data_devolucao

    def get_livro(self) -> Livro:
        return self.livro
    
    def get_usuario(self) -> Usuario:
        return self.usuario

    def to_string(self) -> str:
        return f"ID: {self.get_id_emprestimo()} | Livro: {self.get_livro().get_titulo()} | Usuário: {self.get_usuario().get_nome()} | Data Empréstimo: {self.get_data_emprestimo()} | Data Devolução: {self.get_data_devolucao()}"
    
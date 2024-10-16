class Funcionario:
    def __init__(self, id_funcionario, nome, cargo):
        self.__id_funcionario = id_funcionario
        self.__nome = nome
        self.__cargo = cargo

    def get_id_funcionario(self):
        return self.__id_funcionario

    def get_nome(self):
        return self.__nome

    def get_cargo(self):
        return self.__cargo

    def set_nome(self, nome):
        self.__nome = nome

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def __str__(self):
        return f"Funcionario[ID: {self.__id_funcionario}, Nome: {self.__nome}, Cargo: {self.__cargo}]"
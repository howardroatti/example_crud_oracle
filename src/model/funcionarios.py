class Funcionario:
    def __init__(self, codigo_funcionario, nome, cargo):
        self.__codigo_funcionario = codigo_funcionario
        self.__nome = nome
        self.__cargo = cargo

    def get_codigo_funcionario(self):
        return self.__codigo_funcionario

    def get_nome(self):
        return self.__nome

    def get_cargo(self):
        return self.__cargo

    def set_nome(self, nome):
        self.__nome = nome

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def __str__(self):
        return f"Funcionario[ID: {self.__codigo_funcionario}, Nome: {self.__nome}, Cargo: {self.__cargo}]"
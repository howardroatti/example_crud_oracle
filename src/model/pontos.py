class Ponto:
    def __init__(self, id_ponto, data, hora_entrada, hora_saida, funcionario):
        self.__id_ponto = id_ponto
        self.__data = data
        self.__hora_entrada = hora_entrada
        self.__hora_saida = hora_saida
        self.__funcionario = funcionario

    def get_id_ponto(self):
        return self.__id_ponto

    def get_data(self):
        return self.__data

    def get_hora_entrada(self):
        return self.__hora_entrada

    def get_hora_saida(self):
        return self.__hora_saida

    def get_funcionario(self):
        return self.__funcionario

    def set_data(self, data):
        self.__data = data

    def set_hora_entrada(self, hora_entrada):
        self.__hora_entrada = hora_entrada

    def set_hora_saida(self, hora_saida):
        self.__hora_saida = hora_saida

    def set_funcionario(self, funcionario):
        self.__funcionario = funcionario

    def __str__(self):
        return (f"Ponto[ID: {self.__id_ponto}, Data: {self.__data}, "
                f"Entrada: {self.__hora_entrada}, Saída: {self.__hora_saida}, "
                f"Funcionário: {self.__funcionario.get_nome()}]")

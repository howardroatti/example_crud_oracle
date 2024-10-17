import pandas as pd

class Ponto:
    def __init__(self, codigo_ponto, data_ponto, hora_entrada, hora_saida, funcionario):
        self.__codigo_ponto = codigo_ponto
        self.__data_ponto = data_ponto
        self.__hora_entrada = hora_entrada
        self.__hora_saida = hora_saida
        self.__funcionario = funcionario

    def get_codigo_ponto(self):
        return self.__codigo_ponto

    def get_data_ponto(self):
        return self.__data_ponto

    def get_hora_entrada(self):
        return self.__hora_entrada

    def get_hora_saida(self):
        return self.__hora_saida

    def get_funcionario(self):
        return self.__funcionario

    def set_data_ponto(self, data_ponto):
        self.__data_ponto = data_ponto

    def set_hora_entrada(self, hora_entrada):
        self.__hora_entrada = hora_entrada

    def set_hora_saida(self, hora_saida):
        self.__hora_saida = hora_saida

    def set_funcionario(self, funcionario):
        self.__funcionario = funcionario

    def __str__(self):
        # Convertendo os tipos numpy.datetime64 para datetime
        data_formatada = pd.to_datetime(self.get_data_ponto()).strftime('%Y-%m-%d')
        hora_entrada_formatada = pd.to_datetime(self.get_hora_entrada()).strftime('%H:%M')
        hora_saida_formatada = pd.to_datetime(self.get_hora_saida()).strftime('%H:%M')

        return (f"Ponto[ID: {self.get_codigo_ponto()}, Data: {data_formatada}, "
                f"Entrada: {hora_entrada_formatada}, Saída: {hora_saida_formatada}, "
                f"Funcionário: {self.get_funcionario().get_nome()}]")

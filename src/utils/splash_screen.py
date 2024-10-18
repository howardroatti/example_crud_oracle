from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        self.qry_total_pontos = config.QUERY_COUNT.format(tabela="pontos")
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        self.created_by = "Pierry Jonny, Maria Eduarda, Matheus Castro, Kaylane Simões e Mylena Leite"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"

    def get_total_pontos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_pontos)["total_pontos"].values[0]

    def get_total_funcionarios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_funcionarios)["total_funcionarios"].values[0]

    def get_updated_screen(self):
        return f"""
    #################################################################################################################
    #                                          SISTEMA DE CONTROLE DE PONTO                                         #
    #                                                                                                               #
    #  TOTAL DE REGISTROS:                                                                                          #
    #      1 - PONTOS: {str(self.get_total_pontos()).ljust(93)}#
    #      2 - FUNCIONARIOS: {str(self.get_total_funcionarios()).ljust(87)}#
    #                                                                                                               #
    #  CRIADO POR: {self.created_by.ljust(97)}#
    #                                                                                                               #
    #  PROFESSOR:  {self.professor.ljust(97)}#
    #                                                                                                               #
    #  DISCIPLINA: {self.disciplina.ljust(97)}#
    #              {self.semestre.ljust(97)}#
    #                                                                                                               #
    #################################################################################################################
    """

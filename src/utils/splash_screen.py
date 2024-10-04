from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_pontos = config.QUERY_COUNT.format(tabela="pontos")
        self.qry_total_funcionarios = config.QUERY_COUNT.format(tabela="funcionarios")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Pierry Jonny, Maria Eduarda, Matheus Castro, Kaylane Simões e Mylena Leite"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/3"

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
        ########################################################
        #                   SISTEMA DE CONTROLE DE PONTO                    
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PONTOS:         {str(self.get_total_pontos()).rjust(5)}
        #      2 - FUNCIONARIOS:         {str(self.get_total_funcionarios()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """

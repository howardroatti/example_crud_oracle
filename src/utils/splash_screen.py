from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_livros = config.QUERY_COUNT.format(tabela="livros")
        self.qry_total_usuarios = config.QUERY_COUNT.format(tabela="usuarios")
        self.qry_total_emprestimos = config.QUERY_COUNT.format(tabela="emprestimos")
        self.qry_total_devolucoes = config.QUERY_COUNT.format(tabela="devolucoes")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = """
        #       CAIO FELIPE CARDOZO DO ESPIRITO SANTO
        #       GUILHERME FERRAZ THOMÉ CASSIS DE OLIVEIRA
        #       GUSTAVO SOARES PRADO
        #       LUIZ FELIPE MACEDO CRUZ
        #       PEDRO HENRIQUE MARINHO DE OLIVEIRA
        #       VINÍCIUS DIAS DE OLIVEIRA"""
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_livros(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_livros)["total_livros"].values[0]

    def get_total_usuarios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_usuarios)["total_usuarios"].values[0]

    def get_total_emprestimos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_emprestimos)["total_emprestimos"].values[0]

    def get_total_devolucoes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_devolucoes)["total_devolucoes"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #       SISTEMA DE GESTÃO DE BIBLIOTECA ESCOLAR
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - LIVROS:      {str(self.get_total_livros()).rjust(5)}
        #      2 - USUÁRIOS:    {str(self.get_total_usuarios()).rjust(5)}
        #      3 - EMPRÉSTIMOS: {str(self.get_total_emprestimos()).rjust(5)}
        #      4 - DEVOLUÇÕES:  {str(self.get_total_devolucoes()).rjust(5)}
        #
        #  GRUPO: {self.created_by}
        #
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        #  PROFESSOR:  {self.professor}
        ########################################################
        """
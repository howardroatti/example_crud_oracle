from conexion.oracle_queries import OracleQueries

class SplashScreen:

    def __init__(self):
        self.qry_total_produtos = "select count(1) as total_produtos from produtos"
        self.qry_total_clientes = "select count(1) as total_clientes from clientes"
        self.qry_total_fornecedores = "select count(1) as total_fornecedores from fornecedores"
        self.qry_total_pedidos = "select count(1) as total_pedidos from pedidos"
        self.qry_total_itens_pedido = "select count(1) as total_itens_pedido from itens_pedido"
        self.created_by = "Howard Roatti"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]

    def get_total_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_clientes"].values[0]

    def get_total_fornecedores(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_fornecedores)["total_fornecedores"].values[0]

    def get_total_pedidos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_pedidos)["total_pedidos"].values[0]

    def get_total_itens_pedidos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_itens_pedido)["total_itens_pedido"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:         {str(self.get_total_produtos()).rjust(5)}
        #      2 - CLIENTES:         {str(self.get_total_clientes()).rjust(5)}
        #      3 - FORNECEDORES:     {str(self.get_total_fornecedores()).rjust(5)}
        #      4 - PEDIDOS:          {str(self.get_total_pedidos()).rjust(5)}
        #      5 - ITENS DE PEDIDOS: {str(self.get_total_itens_pedidos()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
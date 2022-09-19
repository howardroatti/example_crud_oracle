from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_pedidos.sql") as f:
            self.query_relatorio_pedidos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_pedidos_por_fornecedor.sql") as f:
            self.query_relatorio_pedidos_por_fornecedor = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_produtos.sql") as f:
            self.query_relatorio_produtos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_fornecedores.sql") as f:
            self.query_relatorio_fornecedores = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_itens_pedidos.sql") as f:
            self.query_relatorio_itens_pedidos = f.read()

    def get_relatorio_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pedidos))
        input("Pressione Enter para Sair do Relatório de Pedidos")

    def get_relatorio_pedidos_por_fornecedor(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pedidos_por_fornecedor))
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para Sair do Relatório de Produtos")

    def get_relatorio_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para Sair do Relatório de Clientes")

    def get_relatorio_fornecedores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores))
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_itens_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_itens_pedidos))
        input("Pressione Enter para Sair do Relatório de Itens de Pedidos")
from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("sql/relatorio_pedidos.sql") as f:
            self.query_relatorio_pedidos = f.read()

        with open("sql/relatorio_pedidos_por_fornecedor.sql") as f:
            self.query_relatorio_pedidos_por_fornecedor = f.read()

        with open("sql/relatorio_produtos.sql") as f:
            self.query_relatorio_produtos = f.read()

        with open("sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()

        with open("sql/relatorio_fornecedores.sql") as f:
            self.query_relatorio_fornecedores = f.read()

        with open("sql/relatorio_itens_pedidos.sql") as f:
            self.query_relatorio_itens_pedidos = f.read()

    def get_relatorio_pedidos(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_pedidos))
        input("Pressione Enter para Sair do Relatório de Pedidos")

    def get_relatorio_pedidos_por_fornecedor(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_pedidos_por_fornecedor))
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_produtos))
        input("Pressione Enter para Sair do Relatório de Produtos")

    def get_relatorio_clientes(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para Sair do Relatório de Clientes")

    def get_relatorio_fornecedores(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores))
        input("Pressione Enter para Sair do Relatório de Fornecedores")

    def get_relatorio_itens_pedidos(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_itens_pedidos))
        input("Pressione Enter para Sair do Relatório de Itens de Pedidos")
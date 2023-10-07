from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_livros_quantidade.sql") as f:
            self.query_relatorio_livros = f.read()

        with open("sql/relatorio_livros_disponiveis.sql") as f:
            self.query_relatorio_livros_disponiveis = f.read()

        with open("sql/relatorio_usuarios_livros.sql") as f:
            self.query_relatorio_usuarios = f.read()

        with open("sql/relatorio_emprestimos_detail.sql") as f:
            self.query_relatorio_emprestimos = f.read()

        with open("sql/relatorio_devolucoes.sql") as f:
            self.query_relatorio_devolucoes = f.read()


        # # Abre o arquivo com a consulta e associa a um atributo da classe
        # with open("sql/relatorio_pedidos.sql") as f:
        #     self.query_relatorio_pedidos = f.read()

        # # Abre o arquivo com a consulta e associa a um atributo da classe
        # with open("sql/relatorio_pedidos_por_fornecedor.sql") as f:
        #     self.query_relatorio_pedidos_por_fornecedor = f.read()

        # # Abre o arquivo com a consulta e associa a um atributo da classe
        # with open("sql/relatorio_produtos.sql") as f:
        #     self.query_relatorio_produtos = f.read()

        # # Abre o arquivo com a consulta e associa a um atributo da classe
        # with open("sql/relatorio_clientes.sql") as f:
        #     self.query_relatorio_clientes = f.read()

        # # Abre o arquivo com a consulta e associa a um atributo da classe
        # with open("sql/relatorio_fornecedores.sql") as f:
        #     self.query_relatorio_fornecedores = f.read()

        # # Abre o arquivo com a consulta e associa a um atributo da classe
        # with open("sql/relatorio_itens_pedidos.sql") as f:
        #     self.query_relatorio_itens_pedidos = f.read()


    def get_relatorio_livros(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_livros))

    def get_relatorio_livros_disponiveis(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_livros_disponiveis))

    def get_relatorio_usuarios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_usuarios))

    def get_relatorio_emprestimos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_emprestimos))

    def get_relatorio_emprestimos_pendentes_por_usuario(self, codigo_usuario) -> bool:        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        #print(oracle.sqlToDataFrame(f"select id_emprestimo, id_livro, id_usuario, data_emprestimo, data_devolucao_sugerida from emprestimos where id_usuario = {codigo_usuario}"))
        #obtém emprestimos do usuário informado que ainda não tenham sido devolvidos
        dataframe = oracle.sqlToDataFrame(f"SELECT empr.* FROM emprestimos empr LEFT JOIN devolucoes devol ON empr.id_emprestimo = devol.id_emprestimo WHERE devol.id_emprestimo IS NULL AND empr.id_usuario = {codigo_usuario}")
        if dataframe.empty:
            print("\nNão existem devoluções pendentes para este usuário.")
        else:
            print(dataframe)
        #retorna se a consulta foi vazia, para saber se existem registros baseados neste usuario
        return not dataframe.empty
    
    def get_relatorio_devolucoes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_devolucoes))

    # def get_relatorio_pedidos(self):
    #     # Cria uma nova conexão com o banco que permite alteração
    #     oracle = OracleQueries()
    #     oracle.connect()
    #     # Recupera os dados transformando em um DataFrame
    #     print(oracle.sqlToDataFrame(self.query_relatorio_pedidos))
    #     input("Pressione Enter para fechar do Relatório")

    # def get_relatorio_pedidos_por_fornecedor(self):
    #     # Cria uma nova conexão com o banco que permite alteração
    #     oracle = OracleQueries()
    #     oracle.connect()
    #     # Recupera os dados transformando em um DataFrame
    #     print(oracle.sqlToDataFrame(self.query_relatorio_pedidos_por_fornecedor))
    #     input("Pressione Enter para Sair do Relatório de Fornecedores")

    # def get_relatorio_clientes(self):
    #     # Cria uma nova conexão com o banco que permite alteração
    #     oracle = OracleQueries()
    #     oracle.connect()
    #     # Recupera os dados transformando em um DataFrame
    #     print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
    #     input("Pressione Enter para Sair do Relatório de Clientes")

    # def get_relatorio_fornecedores(self):
    #     # Cria uma nova conexão com o banco que permite alteração
    #     oracle = OracleQueries()
    #     oracle.connect()
    #     # Recupera os dados transformando em um DataFrame
    #     print(oracle.sqlToDataFrame(self.query_relatorio_fornecedores))
    #     input("Pressione Enter para Sair do Relatório de Fornecedores")

    # def get_relatorio_itens_pedidos(self):
    #     # Cria uma nova conexão com o banco que permite alteração
    #     oracle = OracleQueries()
    #     oracle.connect()
    #     # Recupera os dados transformando em um DataFrame
    #     print(oracle.sqlToDataFrame(self.query_relatorio_itens_pedidos))
    #     input("Pressione Enter para Sair do Relatório de Itens de Pedidos")
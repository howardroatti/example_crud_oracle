from model.produtos import Produto
from conexion.oracle_queries import OracleQueries

class Controller_Produto:
    def __init__(self):
        pass
        
    def inserir_produto(self) -> Produto:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        #Solicita ao usuario a nova descrição do produto
        descricao_novo_produto = input("Descrição (Novo): ")

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, descricao_produto=descricao_novo_produto)
        # Executa o bloco PL/SQL anônimo para inserção do novo produto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := PRODUTOS_CODIGO_PRODUTO_SEQ.NEXTVAL;
            insert into produtos values(:codigo, :descricao_produto);
        end;
        """, data)
        # Recupera o código do novo produto
        codigo_produto = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo_produto}")
        # Cria um novo objeto Produto
        novo_produto = Produto(df_produto.codigo_produto.values[0], df_produto.descricao_produto.values[0])
        # Exibe os atributos do novo produto
        print(novo_produto.to_string())
        # Retorna o objeto novo_produto para utilização posterior, caso necessário
        return novo_produto

    def atualizar_produto(self) -> Produto:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_produto = int(input("Código do Produto que irá alterar: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_produto(oracle, codigo_produto):
            # Solicita a nova descrição do produto
            nova_descricao_produto = input("Descrição (Novo): ")
            # Atualiza a descrição do produto existente
            oracle.write(f"update produtos set descricao_produto = '{nova_descricao_produto}' where codigo_produto = {codigo_produto}")
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo_produto}")
            # Cria um novo objeto Produto
            produto_atualizado = Produto(df_produto.codigo_produto.values[0], df_produto.descricao_produto.values[0])
            # Exibe os atributos do novo produto
            print(produto_atualizado.to_string())
            # Retorna o objeto produto_atualizado para utilização posterior, caso necessário
            return produto_atualizado
        else:
            print(f"O código {codigo_produto} não existe.")
            return None

    def excluir_produto(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do produto a ser alterado
        codigo_produto = int(input("Código do Produto que irá excluir: "))        

        # Verifica se o produto existe na base de dados
        if not self.verifica_existencia_produto(oracle, codigo_produto):            
            # Recupera os dados do novo produto criado transformando em um DataFrame
            df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo_produto}")
            # Revome o produto da tabela
            oracle.write(f"delete from produtos where codigo_produto = {codigo_produto}")            
            # Cria um novo objeto Produto para informar que foi removido
            produto_excluido = Produto(df_produto.codigo_produto.values[0], df_produto.descricao_produto.values[0])
            # Exibe os atributos do produto excluído
            print("Produto Removido com Sucesso!")
            print(produto_excluido.to_string())
        else:
            print(f"O código {codigo_produto} não existe.")

    def verifica_existencia_produto(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados do novo produto criado transformando em um DataFrame
        df_produto = oracle.sqlToDataFrame(f"select codigo_produto, descricao_produto from produtos where codigo_produto = {codigo}")
        return df_produto.empty
from model.livro import Livro
from conexion.oracle_queries import OracleQueries

class Controller_Livro:
    def __init__(self):
        pass
        
    def inserir_livro(self) -> Livro:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        #Solicita ao usuario os dados do livro
        print("Insira os dados do livro a ser cadastrado.\n")
        titulo_novo_livro = input("Título: ")
        autor_novo_livro = input("Autor: ")
        ano_novo_livro = int(input("Ano de publicação (número): "))
        qtd_novo_livro = int(input("Quantidade (número): "))

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, titulo=titulo_novo_livro, autor=autor_novo_livro, ano=ano_novo_livro, qtd=qtd_novo_livro)
        # Executa o bloco PL/SQL anônimo para inserção do novo livro e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := LIVROS_ID_LIVRO_SEQ.NEXTVAL;
            insert into livros values(:codigo, :titulo, :autor, :ano, :qtd, :qtd);
        end;
        """, data)
        # Recupera o código do novo livro
        id_livro = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados do novo livro criado transformando em um DataFrame
        novo_livro = self.get_livro_from_dataframe(oracle, id_livro)
        # Exibe os atributos do novo livro
        print(novo_livro.to_string())
        # Retorna o objeto livro para utilização posterior, caso necessário
        return novo_livro

    def atualizar_livro(self) -> Livro:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do livro a ser alterado
        id_livro = int(input("Código do Livro que irá alterar: "))        

        # Verifica se o livro existe na base de dados
        if not self.verifica_existencia_livro(oracle, id_livro):
            print("Insira os novos dados do livro a ser atualizado.\n")
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de publicação (número): "))
            qtd = int(input("Quantidade (número): "))
            disponibilidade = int(input("Disponibilidade (número): "))

            # Atualiza a descrição do livro existente
            oracle.write(f"update livros set titulo = '{titulo}', autor = '{autor}', ano_publicacao = '{ano}', quantidade = '{qtd}', disponibilidade = '{disponibilidade}' where id_livro = {id_livro}")

            # Cria um novo objeto Livro
            livro_atualizado = self.get_livro_from_dataframe(oracle, id_livro)

            # Exibe os atributos do novo livro
            print(livro_atualizado.to_string())

            # Retorna o objeto livro_atualizado para utilização posterior, caso necessário
            return livro_atualizado
        else:
            print(f"O código {id_livro} não existe.")
            return None

    def excluir_livro(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da entidade a ser alterada
        id_livro = int(input("Código do Livro que irá excluir: "))        

        # Verifica se a entidade existe na base de dados
        if not self.verifica_existencia_livro(oracle, id_livro):            
            # Recupera os dados da entidade e cria um novo objeto para informar que foi removido
            livro_excluido = self.get_livro_from_dataframe(oracle, id_livro)
            # Revome da tabela
            oracle.write(f"delete from livros where id_livro = {id_livro}")            
            # Exibe os atributos do objeto excluído
            print("Livro Removido com Sucesso!")
            print(livro_excluido.to_string())
        else:
            print(f"O código {id_livro} não existe.")

    def verifica_existencia_livro(self, oracle:OracleQueries, id_livro:int=None) -> bool:
        # Recupera os dados da nova entidade criada transformando em um DataFrame
        df_livro = oracle.sqlToDataFrame(f"select id_livro, titulo, autor, ano_publicacao, quantidade, disponibilidade from livros where id_livro = {id_livro}")
        return df_livro.empty
    
    def get_livro_from_dataframe(self, oracle:OracleQueries, id_livro:int=None) -> Livro:
        # Recupera os dados do novo livro criado transformando em um DataFrame
        df_livro = oracle.sqlToDataFrame(f"select id_livro, titulo, autor, ano_publicacao, quantidade, disponibilidade from livros where id_livro = {id_livro}")
        # Cria novo objeto a partir do DataFrame
        novo_livro = Livro(df_livro.id_livro.values[0], df_livro.titulo.values[0], df_livro.autor.values[0], df_livro.ano_publicacao.values[0], df_livro.quantidade.values[0], df_livro.disponibilidade.values[0])
        return novo_livro
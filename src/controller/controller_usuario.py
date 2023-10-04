from model.usuario import Usuario
from conexion.oracle_queries import OracleQueries

class Controller_Usuario:
    def __init__(self):
        pass
        
    def inserir_usuario(self) -> Usuario:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        #Solicita os dados de cadastro
        print("Insira os dados do usuário.\n")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, nome=nome, email=email, telefone=telefone)
        # Executa o bloco PL/SQL anônimo para inserção do novo objeto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := USUARIOS_ID_USUARIO_SEQ.NEXTVAL;
            insert into usuarios values(:codigo, :nome, :email, :telefone);
        end;
        """, data)
        # Recupera o código da nova entidade
        id_usuario = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados da nova entidade criada transformando em um DataFrame
        novo_usuario = Controller_Usuario.get_usuario_from_dataframe(oracle, id_usuario)
        # Exibe os atributos do novo objeto
        print(novo_usuario.to_string())
        # Retorna o objeto para utilização posterior, caso necessário
        return novo_usuario

    def atualizar_usuario(self) -> Usuario:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da entidade a ser alterada
        id_usuario = int(input("Código do Usuário que irá alterar: "))        

        # Verifica se a entidade existe na base de dados
        if Controller_Usuario.verifica_existencia_usuario(oracle, id_usuario):
            print("Insira os novos dados do usuário a ser atualizado.\n")
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")

            # Atualiza os dados da entidade existente
            oracle.write(f"update usuarios set nome = '{nome}', email = '{email}', telefone = '{telefone}' where id_usuario = {id_usuario}")

            # Cria um novo objeto atualizado
            usuario_atualizado = Controller_Usuario.get_usuario_from_dataframe(oracle, id_usuario)

            # Exibe os atributos do novo objeto
            print(usuario_atualizado.to_string())

            # Retorna o objeto para utilização posterior, caso necessário
            return usuario_atualizado
        else:
            print(f"O código {id_usuario} não existe.")
            return None

    def excluir_usuario(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da entidade a ser alterada
        id_usuario = int(input("Código do Usuário que irá excluir: "))        

        # Verifica se a entidade existe na base de dados
        if Controller_Usuario.verifica_existencia_usuario(oracle, id_usuario):            
            # Recupera os dados da entidade e cria um novo objeto para informar que foi removido
            usuario_excluido = Controller_Usuario.get_usuario_from_dataframe(oracle, id_usuario)
            # Revome da tabela
            oracle.write(f"delete from usuarios where id_usuario = {id_usuario}")
            # Exibe os atributos do objeto excluído
            print("Usuario Removido com Sucesso!")
            print(usuario_excluido.to_string())
        else:
            print(f"O código {id_usuario} não existe.")

    @staticmethod
    def verifica_existencia_usuario(oracle:OracleQueries, id_usuario:int=None) -> bool:
        # Recupera os dados da nova entidade criada transformando em um DataFrame
        df_usuario = oracle.sqlToDataFrame(f"select id_usuario, nome, email, telefone from usuarios where id_usuario = {id_usuario}")
        return not df_usuario.empty
    
    @staticmethod
    def get_usuario_from_dataframe(oracle:OracleQueries, id_usuario:int=None) -> Usuario:
        # Recupera os dados transformando em um DataFrame
        df_usuario = oracle.sqlToDataFrame(f"select id_usuario, nome, email, telefone from usuarios where id_usuario = {id_usuario}")
        # Cria novo objeto a partir do DataFrame
        return Usuario(df_usuario.id_usuario.values[0], df_usuario.nome.values[0], df_usuario.email.values[0], df_usuario.telefone.values[0])
    
    @staticmethod
    def valida_usuario(oracle:OracleQueries, codigo_usuario:int=None) -> Usuario:
        if not Controller_Usuario.verifica_existencia_usuario(oracle, codigo_usuario):
            print(f"O usuário de código {codigo_usuario} não existe na base.")
            return None
        else:
            return Controller_Usuario.get_usuario_from_dataframe(oracle, codigo_usuario)
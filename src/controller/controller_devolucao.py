from model.emprestimo import Emprestimo
from model.devolucao import Devolucao
from controller.controller_usuario import Controller_Usuario
from controller.controller_emprestimo import Controller_Emprestimo
from conexion.oracle_queries import OracleQueries

from reports.relatorios import Relatorio

class Controller_Devolucao:

    def __init__(self):
        self.relatorio = Relatorio()
        self.ctrl_emprestimo = Controller_Emprestimo()

    def inserir_devolucao(self) -> Devolucao:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries()
        # Recupera o cursos para executar um bloco PL/SQL anônimo
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        devolucao_cadastrada = self.cadastrar_devolucao(oracle)
        if(devolucao_cadastrada == None):
            return None

        id_emprestimo = devolucao_cadastrada.get_emprestimo().get_id_emprestimo()
        data_devolucao = devolucao_cadastrada.get_data_devolucao()

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, id_emprestimo=int(id_emprestimo), data_devolucao=data_devolucao)
        # Executa o bloco PL/SQL anônimo para inserção do novo objeto e recuperação da chave primária criada pela sequence
        cursor.execute("""
        begin
            :codigo := DEVOLUCOES_ID_DEVOLUCAO_SEQ.NEXTVAL;
            insert into devolucoes values(:codigo, :id_emprestimo, to_date(:data_devolucao,'DD/MM/YYYY'));
        end;
        """, data)
        # Recupera o código da nova entidade
        id_devolucao = output_value.getvalue()
        # Persiste (confirma) as alterações
        oracle.conn.commit()
        # Recupera os dados da nova entidade criada transformando em um DataFrame
        nova_devolucao = Controller_Devolucao.get_devolucao_from_dataframe(oracle, id_devolucao)
        # Exibe os atributos do novo objeto
        print(nova_devolucao.to_string())
        # Retorna o objeto para utilização posterior, caso necessário
        return nova_devolucao

    def atualizar_devolucao(self) -> Devolucao:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da entidade a ser alterada
        id_devolucao = int(input("Código da Devolução que irá alterar: "))        

        # Verifica se a entidade existe na base de dados
        if Controller_Devolucao.verifica_existencia_devolucao(oracle, id_devolucao):
            self.relatorio.get_relatorio_emprestimos()
            codigo_emprestimo = str(input("\nDigite o novo código do empréstimo: "))
            emprestimo = Controller_Emprestimo.valida_emprestimo(oracle, codigo_emprestimo)
            if emprestimo == None:
                return None

            data_devolucao = input("Digite a nova Data da devolução (DD/MM/YYYY): ")

            devolucao_cadastrada = Devolucao(0, emprestimo, data_devolucao)

            # Atualiza os dados da entidade existente
            oracle.write(f"update devolucoes set id_emprestimo = '{devolucao_cadastrada.get_emprestimo().get_id_emprestimo()}', data_devolucao = to_date('{devolucao_cadastrada.get_data_devolucao()}','DD/MM/YYYY') where id_devolucao = {id_devolucao}")

            # Cria um novo objeto atualizado
            devolucao_atualizada = Controller_Devolucao.get_devolucao_from_dataframe(oracle, id_devolucao)

            # Exibe os atributos do novo objeto
            print(devolucao_atualizada.to_string())

            # Retorna o objeto para utilização posterior, caso necessário
            return devolucao_atualizada
        else:
            print(f"O código {id_devolucao} não existe.")
            return None

    def excluir_devolucao(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código da entidade a ser alterada
        id_devolucao = int(input("Código da Devolução que irá excluir: "))        

        # Verifica se a entidade existe na base de dados
        if Controller_Devolucao.verifica_existencia_devolucao(oracle, id_devolucao):            
            # Recupera os dados da entidade e cria um novo objeto para informar que foi removido
            devolucao_excluida = Controller_Devolucao.get_devolucao_from_dataframe(oracle, id_devolucao)
            # Revome da tabela
            oracle.write(f"delete from devolucoes where id_devolucao = {id_devolucao}")
            # Exibe os atributos do objeto excluído
            print("Devolução removida com Sucesso!")
            print(devolucao_excluida.to_string())
        else:
            print(f"O código de Devolução {id_devolucao} não existe.")

    def cadastrar_devolucao(self, oracle) -> Devolucao:
        #Solicita os dados de cadastro
        print("Informe os dados solicitado para cadastrar a devolução.\n")

        # Lista os usuarios existentes
        self.relatorio.get_relatorio_usuarios()
        codigo_usuario = str(input("\nDigite o código do usuário a fazer a devolução: "))
        usuario = Controller_Usuario.valida_usuario(oracle, codigo_usuario)
        if usuario == None:            
            return None

        # Lista os empréstimos existentes
        emprestimos_existentes = self.relatorio.get_relatorio_emprestimos_pendentes_por_usuario(codigo_usuario)
        if emprestimos_existentes == False:
            return None
        
        codigo_emprestimo = str(input("\nDigite o código do empréstimo a ser devolvido: "))
        emprestimo = Controller_Emprestimo.valida_emprestimo(oracle, codigo_emprestimo)
        if emprestimo == None:
            return None

        print("\n")

        if not Controller_Devolucao.valida_emprestimo_aberto(oracle, codigo_usuario, codigo_emprestimo):
            print(f"Não foi encontrado neste usuário um empréstimo em aberto com código {codigo_emprestimo}")
            return None

        data_devolucao = input("Data da devolução (DD/MM/YYYY): ")

        return Devolucao(0, emprestimo, data_devolucao)

    @staticmethod
    def verifica_existencia_devolucao(oracle:OracleQueries, id_devolucao:int=None) -> bool:
        # Recupera os dados da nova entidade criada transformando em um DataFrame
        df_devolucao = oracle.sqlToDataFrame(f"select id_devolucao, id_emprestimo, data_devolucao from devolucoes where id_devolucao = {id_devolucao}")
        return not df_devolucao.empty   
    
    @staticmethod
    def get_devolucao_from_dataframe(oracle:OracleQueries, id_devolucao:int=None) -> Devolucao:
        # Recupera os dados transformando em um DataFrame
        df_devolucao = oracle.sqlToDataFrame(f"select id_devolucao, id_emprestimo, data_devolucao from devolucoes where id_devolucao = {id_devolucao}")
        # Cria novo objeto a partir do DataFrame
        emprestimo = Controller_Emprestimo.get_emprestimo_from_dataframe(oracle, int(df_devolucao.id_emprestimo.values[0]))
        return Devolucao(int(df_devolucao.id_devolucao.values[0]), emprestimo, df_devolucao.data_devolucao.values[0])
    
    @staticmethod
    def valida_emprestimo_aberto(oracle:OracleQueries, id_usuario:int=None, id_emprestimo:int=None) -> bool:
        # Recupera os dados da nova entidade criada transformando em um DataFrame
        dataframe = oracle.sqlToDataFrame(f"SELECT empr.* FROM emprestimos empr LEFT JOIN devolucoes devol ON empr.id_emprestimo = devol.id_emprestimo WHERE devol.id_emprestimo IS NULL AND empr.id_usuario = {id_usuario} AND empr.id_emprestimo = {id_emprestimo}")
        return not dataframe.empty

    
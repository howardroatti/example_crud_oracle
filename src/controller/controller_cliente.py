from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Controller_Cliente:
    def __init__(self):
        pass
        
    def inserir_cliente(self) -> Cliente:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CPF
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_cliente(oracle, cpf):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo cliente
            oracle.write(f"insert into clientes values ('{cpf}', '{nome}')")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = '{cpf}'")
            # Cria um novo objeto Cliente
            novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
            # Exibe os atributos do novo cliente
            print(novo_cliente.to_string())
            # Retorna o objeto novo_cliente para utilização posterior, caso necessário
            return novo_cliente
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_cliente(self) -> Cliente:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do cliente a ser alterado
        cpf = int(input("CPF do cliente que deseja alterar o nome: "))

        # Verifica se o cliente existe na base de dados
        if not self.verifica_existencia_cliente(oracle, cpf):
            # Solicita a nova descrição do cliente
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do cliente existente
            oracle.write(f"update clientes set nome = '{novo_nome}' where cpf = {cpf}")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
            # Cria um novo objeto cliente
            cliente_atualizado = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
            # Exibe os atributos do novo cliente
            print(cliente_atualizado.to_string())
            # Retorna o objeto cliente_atualizado para utilização posterior, caso necessário
            return cliente_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_cliente(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do Cliente a ser alterado
        cpf = int(input("CPF do Cliente que irá excluir: "))        

        # Verifica se o cliente existe na base de dados
        if not self.verifica_existencia_cliente(oracle, cpf):            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
            # Revome o cliente da tabela
            oracle.write(f"delete from clientes where cpf = {cpf}")            
            # Cria um novo objeto Cliente para informar que foi removido
            cliente_excluido = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
            # Exibe os atributos do cliente excluído
            print("Cliente Removido com Sucesso!")
            print(cliente_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_cliente(self, oracle:OracleQueries, cpf:str=None) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = {cpf}")
        return df_cliente.empty
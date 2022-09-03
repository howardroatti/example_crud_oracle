from model.fornecedores import Fornecedor
from conexion.oracle_queries import OracleQueries

class Controller_Fornecedor:
    def __init__(self):
        pass
        
    def inserir_fornecedor(self) -> Fornecedor:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o novo CNPJ
        cnpj = input("CNPJ (Novo): ")

        if self.verifica_existencia_fornecedor(oracle, cnpj):
            # Solicita ao usuario a nova razão social
            razao_social = input("Razão Social (Novo): ")
            # Solicita ao usuario o novo nome fantasia
            nome_fantasia = input("Nome Fantasia (Novo): ")
            # Insere e persiste o novo fornecedor
            oracle.write(f"insert into fornecedores values ('{cnpj}', '{razao_social}', '{nome_fantasia}')")
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_fornecedor = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from fornecedores where cnpj = '{cnpj}'")
            # Cria um novo objeto fornecedor
            novo_fornecedor = Fornecedor(df_fornecedor.cnpj.values[0], df_fornecedor.razao_social.values[0], df_fornecedor.nome_fantasia.values[0])
            # Exibe os atributos do novo fornecedor
            print(novo_fornecedor.to_string())
            # Retorna o objeto novo_fornecedor para utilização posterior, caso necessário
            return novo_fornecedor
        else:
            print(f"O CNPJ {cnpj} já está cadastrado.")
            return None

    def atualizar_fornecedor(self) -> Fornecedor:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fornecedor a ser alterado
        cnpj = int(input("CNPJ do fornecedor que deseja atualizar: "))

        # Verifica se o fornecedor existe na base de dados
        if not self.verifica_existencia_fornecedor(oracle, cnpj):
            # Solicita ao usuario a nova razão social
            razao_social = input("Razão Social (Novo): ")
            # Solicita ao usuario o novo nome fantasia
            nome_fantasia = input("Nome Fantasia (Novo): ")            
            # Atualiza o nome do fornecedor existente
            oracle.write(f"update fornecedores set razao_social = '{razao_social}', nome_fantasia = '{nome_fantasia}'  where cnpj = {cnpj}")
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_fornecedor = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from fornecedores where cnpj = {cnpj}")
            # Cria um novo objeto fornecedor
            fornecedor_atualizado = Fornecedor(df_fornecedor.cnpj.values[0], df_fornecedor.razao_social.values[0], df_fornecedor.nome_fantasia.values[0])
            # Exibe os atributos do novo fornecedor
            print(fornecedor_atualizado.to_string())
            # Retorna o objeto fornecedor_atualizado para utilização posterior, caso necessário
            return fornecedor_atualizado
        else:
            print(f"O CNPJ {cnpj} não existe.")
            return None

    def excluir_fornecedor(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do fornecedor a ser alterado
        cnpj = int(input("CNPJ do fornecedor que irá excluir: "))        

        # Verifica se o fornecedor existe na base de dados
        if not self.verifica_existencia_fornecedor(oracle, cnpj):            
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_fornecedor = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from fornecedores where cnpj = {cnpj}")
            # Revome o fornecedor da tabela
            oracle.write(f"delete from fornecedores where cnpj = {cnpj}")            
            # Cria um novo objeto fornecedor para informar que foi removido
            fornecedor_excluido = Fornecedor(df_fornecedor.cnpj.values[0], df_fornecedor.razao_social.values[0], df_fornecedor.nome_fantasia.values[0])
            # Exibe os atributos do fornecedor excluído
            print("fornecedor Removido com Sucesso!")
            print(fornecedor_excluido.to_string())
        else:
            print(f"O CNPJ {cnpj} não existe.")

    def verifica_existencia_fornecedor(self, oracle:OracleQueries, cnpj:str=None) -> bool:
        # Recupera os dados do novo fornecedor criado transformando em um DataFrame
        df_fornecedor = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from fornecedores where cnpj = {cnpj}")
        return df_fornecedor.empty
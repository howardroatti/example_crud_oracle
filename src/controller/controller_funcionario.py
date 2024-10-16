from conexion.oracle_queries import OracleQueries
from model.funcionarios import Funcionario
from model.pontos import Ponto

class Controller_Funcionario:
    def __init__(self):
        pass

    def inserir_funcionario(self) -> Funcionario:
        oracle = OracleQueries()
        oracle.connect()

        nome = input("Nome do Funcionário: ")
        cargo = input("Cargo do Funcionário: ")

        cursor = oracle.connect()
        output_value = cursor.var(int)

        data = dict(id_funcionario=output_value, nome=nome, cargo=cargo)
        cursor.execute("""
        begin
            :id_funcionario := FUNCIONARIOS_ID_FUNCIONARIO_SEQ.NEXTVAL;
            insert into funcionarios (id_funcionario, nome, cargo) values(:id_funcionario, :nome, :cargo);
        end;
        """, data)

        id_funcionario = output_value.getvalue()
        oracle.conn.commit()

        novo_funcionario = Funcionario(id_funcionario, nome, cargo)
        print(novo_funcionario)
        return novo_funcionario

    def atualizar_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("ID do Funcionário que irá alterar: "))

        if not self.verifica_existencia_funcionario(oracle, id_funcionario):
            novo_nome = input("Novo Nome: ")
            novo_cargo = input("Novo Cargo: ")

            oracle.write(f"update funcionarios set nome = '{novo_nome}', cargo = '{novo_cargo}' where id_funcionario = {id_funcionario}")

            df_funcionario = oracle.sqlToDataFrame(f"select id_funcionario, nome, cargo from funcionarios where id_funcionario = {id_funcionario}")
            funcionario_atualizado = Funcionario(df_funcionario.id_funcionario.values[0], df_funcionario.nome.values[0], df_funcionario.cargo.values[0])
            print(funcionario_atualizado)
            return funcionario_atualizado
        else:
            print(f"O ID {id_funcionario} não existe.")
            return None

    def excluir_funcionario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_funcionario = int(input("ID do Funcionário que irá excluir: "))

        if not self.verifica_existencia_funcionario(oracle, id_funcionario):
            oracle.write(f"delete from funcionarios where id_funcionario = {id_funcionario}")
            print("Funcionário removido com sucesso!")
        else:
            print(f"O ID {id_funcionario} não existe.")

    def verifica_existencia_funcionario(self, oracle: OracleQueries, id:int=None) -> bool:
        df_funcionario = oracle.sqlToDataFrame(f"select id_funcionario from funcionarios where id_funcionario = {id}")
        return df_funcionario.empty
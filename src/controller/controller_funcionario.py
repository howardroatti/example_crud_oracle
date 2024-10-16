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

        data = dict(codigo_funcionario=output_value, nome=nome, cargo=cargo)
        cursor.execute("""
        begin
            :codigo_funcionario := FUNCIONARIOS_CODIGO_FUNCIONARIO_SEQ.NEXTVAL;
            insert into funcionarios (codigo_funcionario, nome, cargo) values(:codigo_funcionario, :nome, :cargo);
        end;
        """, data)

        codigo_funcionario = output_value.getvalue()
        oracle.conn.commit()

        novo_funcionario = Funcionario(codigo_funcionario, nome, cargo)
        print(novo_funcionario)
        return novo_funcionario

    def atualizar_funcionario(self) -> Funcionario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_funcionario = int(input("ID do Funcionário que irá alterar: "))

        if not self.verifica_existencia_funcionario(oracle, codigo_funcionario):
            novo_nome = input("Novo Nome: ")
            novo_cargo = input("Novo Cargo: ")

            oracle.write(f"update funcionarios set nome = '{novo_nome}', cargo = '{novo_cargo}' where codigo_funcionario = {codigo_funcionario}")

            df_funcionario = oracle.sqlToDataFrame(f"select codigo_funcionario, nome, cargo from funcionarios where codigo_funcionario = {codigo_funcionario}")
            funcionario_atualizado = Funcionario(df_funcionario.codigo_funcionario.values[0], df_funcionario.nome.values[0], df_funcionario.cargo.values[0])
            print(funcionario_atualizado)
            return funcionario_atualizado
        else:
            print(f"O ID {codigo_funcionario} não existe.")
            return None

    def excluir_funcionario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_funcionario = int(input("ID do Funcionário que irá excluir: "))

        if not self.verifica_existencia_funcionario(oracle, codigo_funcionario):
            oracle.write(f"delete from funcionarios where codigo_funcionario = {codigo_funcionario}")
            print("Funcionário removido com sucesso!")
        else:
            print(f"O código {codigo_funcionario} não existe.")

    def verifica_existencia_funcionario(self, oracle: OracleQueries, id:int=None) -> bool:
        df_funcionario = oracle.sqlToDataFrame(f"select codigo_funcionario from funcionarios where codigo_funcionario = {id}")
        return df_funcionario.empty
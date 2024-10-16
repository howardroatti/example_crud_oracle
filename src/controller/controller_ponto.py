from conexion.oracle_queries import OracleQueries
from model.funcionarios import Funcionario
from model.pontos import Ponto
from controller.controller_funcionario import Controller_Funcionario

class Controller_Ponto:
    def __init__(self):
        self.ctrl_funcionario = Controller_Funcionario()

    def inserir_ponto(self) -> Ponto:
        oracle = OracleQueries()
        oracle.connect()

        codigo_funcionario = int(input("Código do Funcionário: "))
        if not self.ctrl_funcionario.verifica_existencia_funcionario(oracle, codigo_funcionario):
            print(f"O código {codigo_funcionario} não existe.")
            return None

        data = input("Data (YYYY-MM-DD): ")
        hora_entrada = input("Hora de Entrada (HH:MM): ")
        hora_saida = input("Hora de Saída (HH:MM): ")

        cursor = oracle.connect()
        output_value = cursor.var(int)

        data = dict(codigo_ponto=output_value, data=data, hora_entrada=hora_entrada, hora_saida=hora_saida, codigo_funcionario=codigo_funcionario)
        cursor.execute("""
        begin
            :codigo_ponto := PONTOS_CODIGO_PONTO_SEQ.NEXTVAL;
            insert into pontos (codigo_ponto, data, hora_entrada, hora_saida, codigo_funcionario) values(:codigo_ponto, :data, :hora_entrada, :hora_saida, :codigo_funcionario);
        end;
        """, data)

        codigo_ponto = output_value.getvalue()
        oracle.conn.commit()

        novo_ponto = Ponto(codigo_ponto, data, hora_entrada, hora_saida, Funcionario(codigo_funcionario, "", ""))
        print(novo_ponto)
        return novo_ponto

    def atualizar_ponto(self) -> Ponto:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_ponto = int(input("Código do Ponto que irá alterar: "))

        if not self.verifica_existencia_ponto(oracle, codigo_ponto):
            nova_data = input("Nova Data (YYYY-MM-DD): ")
            nova_hora_entrada = input("Nova Hora de Entrada (HH:MM): ")
            nova_hora_saida = input("Nova Hora de Saída (HH:MM): ")

            oracle.write(f"update pontos set data = '{nova_data}', hora_entrada = '{nova_hora_entrada}', hora_saida = '{nova_hora_saida}' where codigo_ponto = {codigo_ponto}")

            df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto, data, hora_entrada, hora_saida, codigo_funcionario from pontos where codigo_ponto = {codigo_ponto}")
            funcionario = Funcionario(df_ponto.codigo_funcionario.values[0], "", "")
            ponto_atualizado = Ponto(df_ponto.codigo_ponto.values[0], df_ponto.data.values[0], df_ponto.hora_entrada.values[0], df_ponto.hora_saida.values[0], funcionario)
            print(ponto_atualizado)
            return ponto_atualizado
        else:
            print(f"O ID {codigo_ponto} não existe.")
            return None

    def excluir_ponto(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_ponto = int(input("Código do Ponto que irá excluir: "))

        if not self.verifica_existencia_ponto(oracle, codigo_ponto):
            oracle.write(f"delete from pontos where codigo_ponto = {codigo_ponto}")
            print("Ponto removido com sucesso!")
        else:
            print(f"O código {codigo_ponto} não existe.")

    def verifica_existencia_ponto(self, oracle: OracleQueries, id:int=None) -> bool:
        df_ponto = oracle.sqlToDataFrame(f"select codigo_ponto from pontos where codigo_ponto = {id}")
        return df_ponto.empty

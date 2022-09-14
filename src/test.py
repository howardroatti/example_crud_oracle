from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(can_write=True)
oracle.connect()
result = oracle.sqlToMatrix("select * from dual")
print(result)

print()

result = oracle.sqlToDataFrame("select * from dual")
print(result)

print()

result = oracle.sqlToJson("select * from dual")
print(result)
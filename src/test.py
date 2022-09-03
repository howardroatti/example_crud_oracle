from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(write=True)
oracle.connect()
result = oracle.sqToMatrix("select * from dual")
print(result)

print()

result = oracle.sqlToDataFrame("select * from dual")
print(result)
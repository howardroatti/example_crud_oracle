from conexion.oracle_queries import OracleQueries

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)            

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Successfully executed")

def run():

    with open("../sql/create_tables_biblioteca.sql") as f:
        query_create = f.read()

    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!")

    with open("../sql/insert_samples_biblioteca.sql") as f:
        query_generate_records = f.read()

    print("Gerenating records")
    generate_records(query=query_generate_records)
    print("Records successfully generated!")

    # with open("../sql/inserting_samples_related_records.sql") as f:
    #     query_generate_related_records = f.read()

    # print("Gerenating records")
    # generate_records(query=query_generate_related_records, sep='--')
    # print("Records successfully generated!")

if __name__ == '__main__':
    run()
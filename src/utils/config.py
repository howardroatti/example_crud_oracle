MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Pontos por Funcionários
2 - Relatório de Pontos
3 - Relatório de Funcionários
0 - Sair
"""

MENU_ENTIDADES = """Opções:
1 - PONTOS
2 - FUNCIONARIOS
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")

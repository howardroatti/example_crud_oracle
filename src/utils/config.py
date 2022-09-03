MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Fornecedores
2 - Relatório de Pedidos
3 - Relatório de Produtos
4 - Relatório de Clientes
5 - Relatório de Fornecedores
6 - Relatório de Itens de Pedidos
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - PRODUTOS
2 - CLIENTES
3 - FORNECEDORES
4 - PEDIDOS
5 - ITENS DE PEDIDOS
"""

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")
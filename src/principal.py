from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_funcionario import Controller_Funcionario
from controller.controller_ponto import Controller_Ponto

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_funcionario = Controller_Funcionario()
ctrl_ponto = Controller_Ponto()

def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_pontos_funcionarios()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_pontos()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_funcionarios()
    else:
        print("Opção inválida. Por favor, insira uma opção disponível no menu")
        

def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        ctrl_ponto.inserir_ponto()
    elif opcao_inserir == 2:
        ctrl_funcionario.inserir_funcionario()
    else:
        print("Opção inválida. Por favor, insira uma opção disponível no menu")
        

def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_pontos()
        ctrl_ponto.atualizar_ponto()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_funcionarios()
        ctrl_funcionario.atualizar_funcionario()
    else:
        print("Opção inválida. Por favor, insira uma opção disponível no menu")

def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        relatorio.get_relatorio_pontos()
        ctrl_ponto.excluir_ponto()
    elif opcao_excluir == 2:
        relatorio.get_relatorio_funcionarios()
        ctrl_funcionario.excluir_funcionario()
    else:
        print("Opção inválida. Por favor, insira uma opção disponível no menu")
        

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1:  # Relatórios
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-3]: "))
            config.clear_console(1)

            reports(opcao_relatorio)
            config.clear_console(1)

        elif opcao == 2:  # Inserir Novos Registros
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)
            config.clear_console(1)
            #print(tela_inicial.get_updated_screen())
            #config.clear_console(1)

        elif opcao == 3:  # Atualizar Registros
            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)
            config.clear_console()

        elif opcao == 4:  # Excluir Registros
            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)
            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console(1)

        elif opcao == 5:
            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            #exit(1)
            config.clear_console(1)

if __name__ == "__main__":
    run()

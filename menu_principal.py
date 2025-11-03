# menu_principal.py
import menu  # importa o menu interno

def mostrar_menu_principal():
    while True:
        print("\n=== Projeto RPG ===")
        print("1) Iniciar Jogo")
        print("2) Carregar Jogo")
        print("3) Opções")
        print("4) Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            carregar_jogo()
        elif escolha == "3":
            opcoes()
        elif escolha == "4":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def iniciar_jogo():
    print("\nIniciando novo jogo...\n")
    menu.menu()  # chama a função principal do menu interno

def carregar_jogo():
    print("\nFunção de carregar jogo ainda não implementada.\n")

def opcoes():
    print("\nConfigurações:\n(futuramente: som, dificuldade, idioma...)\n")

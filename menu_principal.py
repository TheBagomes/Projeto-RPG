import menu  

def mostrar_menu_principal():
    while True:
        print("\n=== Projeto RPG ===")
        print("1) Iniciar Jogo")
        print("2) Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def iniciar_jogo():
     print("\nIniciando novo jogo...\n")
     menu.menu()  



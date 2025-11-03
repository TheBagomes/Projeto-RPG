from menus import menu_atirador, menu_guerreiro, menu_magos, menu_bardo

def menu():
    while True:
        print("=== Criação de Personagem ===")
        print("Escolha uma classe:")
        print("[1] Guerreiro")
        print("[2] Mago")
        print("[3] Atirador")
        print("[4] Bardo")

        resp = int(input("Sua opção: "))

        if resp == 1:
            menu_guerreiro.submenu_guerreiros()
        elif resp == 2:
            menu_magos.submenu_magos()
        elif resp == 3:
            menu_atirador.submenu_ator()
        elif resp == 4:
            menu_bardo.submenu_bardo()
        else:
            print("Opção inválida.")

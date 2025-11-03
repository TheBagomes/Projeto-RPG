# from menus import menu_atirador, menu_guerreiro, menu_magos, menu_bardo

# def menu():
#     while True:
#         print("=== Criação de Personagem ===")
#         print("Escolha uma classe:")
#         print("[1] Guerreiro")
#         print("[2] Mago")
#         print("[3] Atirador")
#         print("[4] Bardo")

#         resp = int(input("Sua opção: "))

#         if resp == 1:
#             menu_guerreiro.submenu_guerreiros()
#         elif resp == 2:
#             menu_magos.submenu_magos()
#         elif resp == 3:
#             menu_atirador.submenu_ator()
#         elif resp == 4:
#             menu_bardo.submenu_bardo()
#         else:
#             print("Opção inválida.")
# menu.py
from database import inserir_personagem, listar_personagens, buscar_personagem_por_id

def menu():
    while True:
        print("\n=== Criação / Gerenciamento de Personagens ===")
        print("1) Criar Guerreiro")
        print("2) Criar Mago")
        print("3) Criar Atirador")
        print("4) Criar Bardo")
        print("5) Listar personagens salvos")
        print("6) Carregar personagem (por ID)")
        print("7) Voltar ao menu principal")
        opc = input("Sua opção: ").strip()

        if opc == "1":
            criar_personagem("Guerreiro")
        elif opc == "2":
            criar_personagem("Mago")
        elif opc == "3":
            criar_personagem("Atirador")
        elif opc == "4":
            criar_personagem("Bardo")
        elif opc == "5":
            listar_todos()
        elif opc == "6":
            carregar_personagem()
        elif opc == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_personagem(classe: str):
    nome = input(f"Digite o nome do seu {classe}: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    pid = inserir_personagem(nome, classe)
    print(f"{classe} '{nome}' criado e salvo com ID {pid}.")

def listar_todos():
    personagens = listar_personagens()
    if not personagens:
        print("Nenhum personagem encontrado.")
        return
    print("\n--- Personagens Salvos ---")
    for p in personagens:
        # p é sqlite3.Row (tem suporte por nome)
        print(f"ID: {p['id']:>3} | Nome: {p['nome']:<15} | Classe: {p['classe']:<10} | Nível: {p['nivel']:<2} | Vida: {p['vida']:<3} | Mana: {p['mana']}")
    print("--------------------------")

def carregar_personagem():
    try:
        pid = int(input("Digite o ID do personagem que deseja carregar: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    p = buscar_personagem_por_id(pid)
    if not p:
        print("Personagem não encontrado.")
        return
    # Aqui você pode converter em uma instância de classe Personagem se existir
    print(f"Carregado -> ID: {p['id']} | Nome: {p['nome']} | Classe: {p['classe']} | Nível: {p['nivel']} | Vida: {p['vida']} | Mana: {p['mana']}")
    # exemplo: iniciar jogo com esse personagem (implemente conforme sua lógica)

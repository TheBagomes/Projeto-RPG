from personagens.guerreiro import Guerreiro
from personagens.magos import Magos
from personagens.atirador import Atirador
from personagens.bardo import Bardo
from database import inserir_personagem, listar_personagens, carregar_personagem
from menus.menu_jogo import batalha


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
            criar_personagem(Guerreiro)
        elif opc == "2":
            criar_personagem(Magos)
        elif opc == "3":
            criar_personagem(Atirador)
        elif opc == "4":
            criar_personagem(Bardo)
        elif opc == "5":
            listar_todos()
        elif opc == "6":
            carregar_personagem()
        elif opc == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")


def criar_personagem(classe_personagem):
    nome = input(f"Digite o nome do seu {classe_personagem.__name__}: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return

    # cria o objeto da classe (ex: Guerreiro(nome))
    personagem = classe_personagem(nome)

    # salva no banco
    inserir_personagem(personagem)

    print(f"{personagem.classe} '{personagem.nome}' criado e salvo no banco!")
    batalha(personagem)


def listar_todos():
    personagens = listar_personagens()
    if not personagens:
        print("Nenhum personagem encontrado.")
        return

    print("\n--- Personagens Salvos ---")
    for p in personagens:
        print(
            f"ID: {p['id']:>3} | Nome: {p['nome']:<15} | Classe: {p['classe']:<10} | "
            f"Nível: {p['nivel']:<2} | Vida: {p['vida']:<3} | Mana: {p['mana']:<3} | Energia: {p['energia']}"
        )
    print("--------------------------")


def carregar_personagem():
    try:
        pid = int(input("Digite o ID do personagem que deseja carregar: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    p = buscar_personagem(pid)
    if not p:
        print("Personagem não encontrado.")
        return

    # recria o personagem com base na classe
    classe = p["classe"]
    if classe == "Guerreiro":
        personagem = Guerreiro(p["nome"])
        personagem.energia = p["energia"]
    elif classe == "Magos":
        personagem = Magos(p["nome"])
        personagem.mana = p["mana"]
    elif classe == "Atirador":
        personagem = Atirador(p["nome"])
        personagem.energia = p["energia"]
    elif classe == "Bardo":
        personagem = Bardo(p["nome"])
        personagem.mana = p["mana"]
    else:
        print("Classe desconhecida.")
        return

    # aplica os atributos salvos
    personagem.vida = p["vida"]
    personagem.vida_max = p["vida_max"]
    personagem.ataque = p["ataque"]
    personagem.defesa = p["defesa"]

    print(f"\n{personagem.classe} '{personagem.nome}' carregado com sucesso!\n")
    batalha(personagem)

from personagens.atirador import Atirador
from menus.menu_jogo import batalha
from database import inserir_personagem

personagens_criados = [] 

def submenu_atirador():
    while True:
        print('=== Escolha sua classe ===')
        print('[1] Arqueiro')
        print('[2] Lançador')
        print('[3] Voltar')
        resp = int(input('Sua opcao: '))

        if resp in [1, 2]:
            criar_personagem(Atirador)
        elif resp == 3:
            break
        else:
            print('Opcão inválida.')

def criar_personagem(classe_personagem):
    nome = input("Digite o nome do personagem: ")
    personagem = classe_personagem(nome)
    personagens_criados.append(personagem)

    inserir_personagem(personagem)
    print(f"{personagem.nome} ({personagem.classe}) criado e salvo no banco!")

    batalha(personagem)

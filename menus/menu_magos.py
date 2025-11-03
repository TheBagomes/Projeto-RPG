from personagens.magos import Magos
from menus.menu_jogo import batalha
from database import inserir_personagem

personagens_criados = [] 

def submenu_magos():
    while True:
        print('=== Escolha sua classe ===')
        print('[1] Mago de Fogo')
        print('[2] Mago de Gelo')
        print('[3] Mago de Raio')
        print('[4] Voltar')
        resp = int(input('Sua opcao: '))

        if resp in [1, 2, 3]:
            criar_personagem(Magos)
        elif resp == 4:
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

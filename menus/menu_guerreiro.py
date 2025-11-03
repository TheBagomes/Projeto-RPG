from personagens.guerreiro import Guerreiro
from menus.menu_jogo import batalha
from database import inserir_personagem

personagens_criados = [] 

def submenu_guerreiros():
    while True:
        print('=== Escolha sua classe ===')
        print('[1] Tank.')
        print('[2] Lutador.')
        print('[3] Voltar.')
        resp = int(input('Sua opcao: '))

        if resp in [1, 2]:
            criar_personagem(Guerreiro)
        elif resp == 3:
            break
        else:
            print('Opcão inválida.')

def criar_personagem(classe_personagem):
    nome = input("Digite o nome do personagem: ")
    personagem = classe_personagem(nome)
    personagens_criados.append(personagem)

    inserir_personagem(personagem)  # <<< SALVA NO BANCO
    print(f"{personagem.nome} ({personagem.classe}) criado e salvo no banco!")

    batalha(personagem)

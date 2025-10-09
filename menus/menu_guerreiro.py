from personagens import guerreiro

personagens_criados = [] 

def submenu_guerreiros(): 
    while True: 
            print('===Escolha sua classe===')
            print('[1] Tank.')
            print('[2] Lutador.')
            print('[3] Voltar.')
            resp = int(input('Sua opcao: '))
            if  resp == 3: 
              break
            p = guerreiro(resp)

def criar_personagem(classe_personagem):
    nome = input("Digite o nome do personagem: ")
    personagem = classe_personagem(nome)
    personagens_criados.append(personagem)
    print(f"{personagem.info()} criado com sucesso!")


def mostrar_personagens():
    if not personagens_criados:
        print("Nenhum personagem criado ainda.")
    else:
        print("\n=== Personagens Criados ===")
        for p in personagens_criados:
            print(p.info())
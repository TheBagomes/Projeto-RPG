from personagens import magos

personagens_criados = [] 

def submenu_magos(): 
    while True: 
            print('===Escolha sua classe===')
            print('[1] Mago de Fogo.')
            print('[2] Mago de Gelo.')
            print('[3] Mago de Raio.')
            print('[4] Voltar.')
            resp2 = int(input('Sua opcao: '))
            if  resp2 == 4: 
              break
            p = magos(resp2)

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


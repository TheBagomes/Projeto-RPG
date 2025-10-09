from personagens import bardo

# personagens_criados = [] 

def submenu_bardo(): 
     
        while True: 
            print('===Escolha sua classe===')
            print('[1] Virtuoso.')
            print('[2] Harpista.')
            print('[3] Voltar.')
            resp4 = int(input('Sua opcao: '))
            if  resp4 == 3: 
              break
            p = bardo(resp4)

# def criar_personagem(classe_personagem):
#     nome = input("Digite o nome do personagem: ")
#     personagem = classe_personagem(nome)
#     personagens_criados.append(personagem)
#     print(f"{personagem.info()} criado com sucesso!")

# def mostrar_personagens():
#     if not personagens_criados:
#         print("Nenhum personagem criado ainda.")
#     else:
#         print("\n=== Personagens Criados ===")
#         for p in personagens_criados:
#             print(p.info())


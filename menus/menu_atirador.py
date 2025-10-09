from personagens import atirador

# personagens_criados = [] 

def submenu_atirador(): 
     while True: 
            print('===Escolha sua classe===')
            print('[1] Arqueiro.')
            print('[2] Lancador.')
            print('[3] Voltar.')
            resp3 = int(input('Sua opcao: '))
            if  resp3 == 3: 
              break
            p = atirador(resp3)

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


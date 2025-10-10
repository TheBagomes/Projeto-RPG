from personagens.magos import Magos

personagens_criados = [] 

def submenu_magos(): 

    while True: 
            print('=== Escolha sua classe ===')
            print('[1] Mago de Fogo.')
            print('[2] Mago de Gelo.')
            print('[3] Mago de Raio.')
            print('[4] Voltar.')
            resp2 = int(input('Sua opcao: '))

            if resp2 == 1: 
              criar_personagem(Magos)
              while True:
                 print('Escolha suas habilidades: ')
                 print('[1] bola de fogo')
                 print('[2] Muralha de chamas') 
                 resp2a = int(input('Seu poder: '))
                 break

            elif resp2 == 2: 
                criar_personagem(Magos)  
            elif resp2 == 3: 
                criar_personagem(Magos)
            elif resp2 == 4: 
                break
            else:
               print('Opcão inválida.')
            break

        
def criar_personagem(classe_personagem):
    nome = input("Digite o nome do personagem: ")
    try:   
      personagem = classe_personagem(nome)
    except Exception as e: 
      print("Erro ao criar personagem.", e)
      return
    
    personagens_criados.append(personagem) 
    
    try: 
     info_texto = personagem.info()
    except Exception: 
     info_texto = getattr(personagem, 'nome', '<sem-nome>')
    
    print(f"{info_texto} criado com sucesso!")   
    
def mostrar_personagens():
    if not personagens_criados:
        print("Nenhum personagem criado ainda.")
    else:
        print("\n=== Personagens Criados ===")
        for p in personagens_criados:
            print(p.info())

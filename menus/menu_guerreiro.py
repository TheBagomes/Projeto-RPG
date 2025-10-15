from personagens.guerreiro import Guerreiro
from menus.menu_jogo import batalha

personagens_criados = [] 

def submenu_guerreiros(): 

    while True: 
            print('=== Escolha sua classe ===')
            print('[1] Tank.')
            print('[2] Lutador.')
            print('[3] Voltar.')
          
            resp = int(input('Sua opcao: '))
            
            if resp == 1: 
              criar_personagem(Guerreiro)
            elif resp == 2: 
                criar_personagem(Guerreiro)  
            elif resp == 3: 
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

    batalha(personagem)
  
    

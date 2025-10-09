from personagens import guerreiro, magos
from menus import menu_guerreiro, menu_magos 

def menu():

    while True:
     print('===Criação de Personagem===')
     print()
     print('Escolha uma classe: ')
     print('[1] Guerreiro.')
     print('[2] Mago.')
     print('[3] Atirador.')
     print('[4] Bardo.')

     resp = int(input('Sua opcão: '))

     if resp == 1  :
      menu_guerreiro.submenu_guerreiros()
        
     if resp == 2 :
        menu_magos.submenu_magos()

     if resp == 3 :
        while True: 
            print('===Escolha sua classe===')
            print('[1] Arqueiro.')
            print('[2] Lancador.')
            print('[3] Voltar.')
            resp3 = int(input('Sua opcao: '))
            if  resp3 == 3: 
              break

     if resp == 4 :
        
        while True: 
            print('===Escolha sua classe===')
            print('[1] Virtuoso.')
            print('[2] Harpista.')
            print('[3] Voltar.')
            resp4 = int(input('Sua opcao: '))
            if  resp4 == 3: 
              break

    print(p.info())

if __name__ == "__main__":
    menu()
from personagens import guerreiro, magos, atirador, bardo
from menus import menu_atirador, menu_guerreiro, menu_magos, menu_bardo

def menu():
    
  while True:
    print('=== Criação de Personagem ===')
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
      menu_atirador.submenu_atirador()
   
    if resp == 4 :
      menu_bardo.submenu_bardo()
         
if __name__ == "__main__":
    menu()
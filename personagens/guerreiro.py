from menus.menu_jogo import batalha

class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.classe = "Guerreiro"
        self.vida = 80
        self.vida_max = 80
        self.ataque = 10
        self.defesa = 5
        self.energia = 30  

    def info(self):
        return f"{self.nome} foi"
      
    def recuperar_energia(self, valor):
        self.energia = min(self.energia + valor, 30)


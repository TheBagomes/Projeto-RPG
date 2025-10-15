class Atirador:
    def __init__(self, nome):
        self.nome = nome
        self.classe = "Atirador"
        self.vida = 80
        self.vida_max = 80
        self.ataque = 10
        self.defesa = 5
        self.energia = 30  

    def info(self):
        return f"{self.nome} foi"
    def recuperar_mana(self, valor):
        self.mana = min(self.mana + valor, 40)
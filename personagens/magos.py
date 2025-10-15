class Magos:
    def __init__(self, nome):
        self.nome = nome
        self.classe = "Magos"
        self.vida = 60
        self.vida_max = 60
        self.ataque = 6
        self.defesa = 3
        self.mana = 40  # usada para magias

    def info(self):
        return f"{self.nome} foi"    

    def recuperar_mana(self, valor):
        self.mana = min(self.mana + valor, 40)
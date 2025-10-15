import random

class Monstro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0


def gerar_monstro():
    monstros = [
        Monstro("Goblin", 30, 6),
        Monstro("Lobo", 25, 5),
        Monstro("Orc", 40, 8)
    ]
    return random.choice(monstros)

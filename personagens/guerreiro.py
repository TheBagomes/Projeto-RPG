class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.classe = "Guerreiro"

    def info(self):
        return f"{self.nome} é um {self.classe}"


# personagens/habilidades.py
import random

def habilidades_guerreiro(jogador, monstro):
    print("\nEscolha uma habilidade:")
    print("[1] Golpe Poderoso (10 energia, causa dano alto)")
    print("[2] Investida (5 energia, dano moderado)")
    print("[3] Cura de Batalha (10 energia, cura 15 de vida)")
    
    escolha = input("→ Sua escolha: ")

    if escolha == "1" and jogador.energia >= 10:
        dano = random.randint(12, 18)
        jogador.energia -= 10
        monstro.vida -= dano
        print(f" {jogador.nome} usou Golpe Poderoso e causou {dano} de dano!")

    elif escolha == "2" and jogador.energia >= 5:
        dano = random.randint(8, 12)
        jogador.energia -= 5
        monstro.vida -= dano
        print(f" {jogador.nome} usou Investida e causou {dano} de dano!")

    elif escolha == "3" and jogador.energia >= 10:
        cura = 15
        jogador.energia -= 10
        jogador.vida = min(jogador.vida + cura, jogador.vida_max)
        print(f" {jogador.nome} usou Cura de Batalha e recuperou {cura} de vida!")

    else:
        print(" Energia insuficiente ou opção inválida!")


def habilidades_mago(jogador, monstro):
    print("\nEscolha uma habilidade:")
    print("[1] Bola de Fogo (10 mana, dano alto)")
    print("[2] Raio Congelante (5 mana, dano médio)")
    print("[3] Cura Mística (10 mana, cura 15 de vida)")
    
    escolha = input("Sua escolha: ")

    if escolha == "1" and jogador.mana >= 10:
        dano = random.randint(14, 20)
        jogador.mana -= 10
        monstro.vida -= dano
        print(f" {jogador.nome} lançou Bola de Fogo e causou {dano} de dano!")

    elif escolha == "2" and jogador.mana >= 5:
        dano = random.randint(8, 12)
        jogador.mana -= 5
        monstro.vida -= dano
        print(f" {jogador.nome} lançou Raio Congelante e causou {dano} de dano!")

    elif escolha == "3" and jogador.mana >= 10:
        cura = 15
        jogador.mana -= 10
        jogador.vida = min(jogador.vida + cura, jogador.vida_max)
        print(f" {jogador.nome} usou Cura Mística e recuperou {cura} de vida!")

    else:
        print("Mana insuficiente ou opção inválida!")

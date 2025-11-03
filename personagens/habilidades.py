import random

def usar_habilidade(jogador, monstro):
    print("\n=== ESCOLHA UMA HABILIDADE ===")

    if jogador.classe == "Guerreiro":
        habilidades_guerreiro(jogador, monstro)
    elif jogador.classe == "Magos":
        habilidades_mago(jogador, monstro)
    elif jogador.classe == "Atirador":
        habilidades_atirador(jogador, monstro)
    elif jogador.classe == "Bardo":
        habilidades_bardo(jogador, monstro)
    else:
        print("Essa classe ainda não tem habilidades definidas.")

# ========================= GUERREIRO =========================
def habilidades_guerreiro(jogador, monstro):
    print("[1] Golpe Poderoso (Custo: 10 energia) — dano alto")
    print("[2] Investida (Custo: 5 energia) — dano moderado")
    print("[3] Recuperar Fôlego (Custo: 10 energia) — cura 20 HP")

    escolha = input("Escolha: ")

    if escolha == "1" and jogador.energia >= 10:
        dano = random.randint(15, 25)
        jogador.energia -= 10
        monstro.vida -= dano
        print(f"{jogador.nome} usou Golpe Poderoso e causou {dano} de dano!")
    elif escolha == "2" and jogador.energia >= 5:
        dano = random.randint(10, 18)
        jogador.energia -= 5
        monstro.vida -= dano
        print(f"{jogador.nome} usou Investida e causou {dano} de dano!")
    elif escolha == "3" and jogador.energia >= 10:
        cura = 20
        jogador.energia -= 10
        jogador.vida = min(jogador.vida + cura, jogador.vida_max)
        print(f"{jogador.nome} recuperou {cura} de vida!")
    else:
        print("Energia insuficiente ou escolha inválida!")

# ========================= MAGO =========================
def habilidades_mago(jogador, monstro):
    if jogador.tipo == "1":
        print("[1] Bola de Fogo (Custo: 15 mana) — dano alto")
        print("[2] Chama Mística (Custo: 10 mana) — dano médio")
        print("[3] Cura Ígnea (Custo: 20 mana) — cura 25 HP")
    elif jogador.tipo == "2":
        print("[1] Lança de Gelo (Custo: 15 mana) — dano médio + defesa temporária")
        print("[2] Nevasca (Custo: 25 mana) — dano alto")
        print("[3] Cura Congelada (Custo: 20 mana) — cura 20 HP")
    elif jogador.tipo == "3":
        print("[1] Raio Elétrico (Custo: 15 mana) — dano médio")
        print("[2] Tempestade (Custo: 25 mana) — dano alto")
        print("[3] Cura Estática (Custo: 20 mana) — cura 20 HP")

    escolha = input("Escolha: ")

    if escolha == "1" and jogador.mana >= 15:
        dano = random.randint(18, 25)
        jogador.mana -= 15
        monstro.vida -= dano
        print(f"{jogador.nome} lançou um ataque mágico e causou {dano} de dano!")
    elif escolha == "2" and jogador.mana >= 25:
        dano = random.randint(25, 35)
        jogador.mana -= 25
        monstro.vida -= dano
        print(f"{jogador.nome} usou um feitiço poderoso e causou {dano} de dano!")
    elif escolha == "3" and jogador.mana >= 20:
        cura = 20
        jogador.mana -= 20
        jogador.vida = min(jogador.vida + cura, jogador.vida_max)
        print(f"{jogador.nome} recuperou {cura} de vida!")
    else:
        print("Mana insuficiente ou escolha inválida!")


# ========================= ATIRADOR =========================
def habilidades_atirador(jogador, monstro):
    print("[1] Tiro Certeiro (Custo: 10 energia) — dano alto")
    print("[2] Disparo Duplo (Custo: 8 energia) — dano médio")
    print("[3] Foco (Custo: 5 energia) — recupera 10 energia")

    escolha = input("Escolha: ")

    if escolha == "1" and jogador.energia >= 10:
        dano = random.randint(15, 25)
        jogador.energia -= 10
        monstro.vida -= dano
        print(f"{jogador.nome} usou Tiro Certeiro e causou {dano} de dano!")
    elif escolha == "2" and jogador.energia >= 8:
        dano = random.randint(10, 18)
        jogador.energia -= 8
        monstro.vida -= dano
        print(f"{jogador.nome} disparou duas flechas e causou {dano} de dano!")
    elif escolha == "3" and jogador.energia >= 5:
        jogador.energia = min(jogador.energia + 10, 60)
        jogador.energia -= 5
        print(f"{jogador.nome} focou sua energia e recuperou parte do vigor!")
    else:
        print("Energia insuficiente ou escolha inválida!")


# ========================= BARDO =========================
def habilidades_bardo(jogador, monstro):
    print("[1] Melodia Afiada (Custo: 10 mana) — dano médio")
    print("[2] Canção Inspiradora (Custo: 15 mana) — aumenta vida em 20")
    print("[3] Acorde Fatal (Custo: 20 mana) — dano alto")

    escolha = input("Escolha: ")

    if escolha == "1" and jogador.mana >= 10:
        dano = random.randint(10, 20)
        jogador.mana -= 10
        monstro.vida -= dano
        print(f"{jogador.nome} tocou Melodia Afiada e causou {dano} de dano!")
    elif escolha == "2" and jogador.mana >= 15:
        cura = 20
        jogador.mana -= 15
        jogador.vida = min(jogador.vida + cura, jogador.vida_max)
        print(f"{jogador.nome} tocou uma canção e recuperou {cura} de vida!")
    elif escolha == "3" and jogador.mana >= 20:
        dano = random.randint(20, 30)
        jogador.mana -= 20
        monstro.vida -= dano
        print(f"{jogador.nome} tocou o Acorde Fatal e causou {dano} de dano!")
    else:
        print("Mana insuficiente ou escolha inválida!")

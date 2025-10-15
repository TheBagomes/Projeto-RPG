import random
import time
from personagens.monstros import gerar_monstro
from personagens.habilidades import usar_habilidade

def rolar_dado(expressao):
    qtd, lados = map(int, expressao.lower().split('d'))
    return sum(random.randint(1, lados) for _ in range(qtd))

def batalha(jogador):
    monstro = gerar_monstro()
    print(f"\n=== BATALHA INICIADA ===")
    print(f"{jogador.nome} ({jogador.classe}) VS {monstro.nome}")
    print(f" Vida do jogador: {jogador.vida} |  Vida do monstro: {monstro.vida}\n")

    while jogador.vida > 0 and monstro.vida > 0:
        input("Pressione ENTER para rolar o dado (1d20)...")
        jogador_rolagem = rolar_dado("1d20")
        monstro_rolagem = rolar_dado("1d20")

        print(f"\n {jogador.nome} rolou {jogador_rolagem}")
        print(f" {monstro.nome} rolou {monstro_rolagem}")

        time.sleep(1)

        
        if jogador_rolagem > monstro_rolagem:      
            dano = random.randint(1, jogador.ataque)
            monstro.vida -= dano
            usar_habilidade(jogador, monstro)
            # print(f"{jogador.nome} atacou e causou {dano} de dano!")
            
        elif monstro_rolagem > jogador_rolagem:
            dano = random.randint(1, monstro.ataque)
            jogador.vida -= dano
            if jogador.vida < 0:
                jogador.vida = 0
            print(f" {monstro.nome} causou {dano} de dano em {jogador.nome}!")
            print(f" Vida restante do jogador: {jogador.vida}")

        else:
            print(" Empate! Nenhum dano causado.")

        time.sleep(1.5)
        print("-" * 30)

    if jogador.vida > 0:
        print(f"\n {jogador.nome} venceu o {monstro.nome}!")
    else:
        print(f"\n {jogador.nome} foi derrotado pelo {monstro.nome}...")

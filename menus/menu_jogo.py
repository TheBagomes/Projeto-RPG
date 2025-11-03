from personagens.monstros import gerar_monstro
from personagens.habilidades import usar_habilidade
from database import atualizar_personagem
import random, time

def batalha(jogador):
    monstro = gerar_monstro()
    print(f"\n=== BATALHA INICIADA ===")
    print(f"{jogador.nome} ({jogador.classe}) VS {monstro.nome}")
    print(f"Vida: {jogador.vida} | Monstro: {monstro.vida}\n")

    while jogador.vida > 0 and monstro.vida > 0:
        input("Pressione ENTER para rolar o dado (1d20)...")
        jogador_rolagem = random.randint(1, 20)
        monstro_rolagem = random.randint(1, 20)

        print(f"\n{jogador.nome} rolou {jogador_rolagem}")
        print(f"{monstro.nome} rolou {monstro_rolagem}")
        time.sleep(1)

        if jogador_rolagem > monstro_rolagem:
            usar_habilidade(jogador, monstro)
        elif monstro_rolagem > jogador_rolagem:
            dano = random.randint(1, monstro.ataque)
            jogador.vida = max(0, jogador.vida - dano)
            print(f"{monstro.nome} causou {dano} de dano! Vida restante: {jogador.vida}")
        else:
            print("Empate!")

        time.sleep(1.5)

    if jogador.vida > 0:
        print(f"\n{jogador.nome} venceu o {monstro.nome}!")
    else:
        print(f"\n{jogador.nome} foi derrotado...")

    atualizar_personagem(jogador)  

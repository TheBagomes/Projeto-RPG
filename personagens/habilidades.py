import random

def usar_habilidade(jogador, monstro, habilidade):
    # Roteador: decide função por classe
    if jogador.classe == "Guerreiro":
        _habilidades_guerreiro(jogador, monstro, habilidade)
    elif jogador.classe == "Magos":
        _habilidades_mago(jogador, monstro, habilidade)
    elif jogador.classe == "Atirador":
        _habilidades_atirador(jogador, monstro, habilidade)
    elif jogador.classe == "Bardo":
        _habilidades_bardo(jogador, monstro, habilidade)
    else:
        # fallback: aplicar dano pequeno
        dano = random.randint(1, max(1, jogador.ataque))
        monstro.vida = max(0, monstro.vida - dano)

# ---------------- GUERREIRO ----------------
def _habilidades_guerreiro(j, m, hab):
    if hab == "Golpe Poderoso" and getattr(j, "energia", 0) >= 10:
        dano = random.randint(15, 25)
        j.energia -= 10
        m.vida = max(0, m.vida - dano)
    elif hab == "Investida" and getattr(j, "energia", 0) >= 5:
        dano = random.randint(10, 18)
        j.energia -= 5
        m.vida = max(0, m.vida - dano)
    elif hab == "Recuperar Fôlego" and getattr(j, "energia", 0) >= 10:
        cura = 20
        j.energia -= 10
        j.vida = min(j.vida + cura, j.vida_max)
    else:
        # falha: nada acontece
        pass

# ---------------- MAGOS ----------------
def _habilidades_mago(j, m, hab):
    tipo = getattr(j, "subtipo", getattr(j, "tipo", "1"))
    # mapa de habilidades por tipo
    if tipo in ["1", "Fogo", "Mago de Fogo"]:
        # Fogo
        if hab == "Bola de Fogo" and j.mana >= 15:
            dano = random.randint(18, 25); j.mana -= 15; m.vida = max(0, m.vida - dano)
        elif hab == "Chama Mística" and j.mana >= 10:
            dano = random.randint(12, 18); j.mana -= 10; m.vida = max(0, m.vida - dano)
        elif hab == "Cura Ígnea" and j.mana >= 20:
            cura = 20; j.mana -= 20; j.vida = min(j.vida + cura, j.vida_max)
    elif tipo in ["2", "Gelo", "Mago de Gelo"]:
        if hab == "Lança de Gelo" and j.mana >= 15:
            dano = random.randint(14, 20); j.mana -= 15; m.vida = max(0, m.vida - dano)
            # poderia aplicar algum buff de defesa no jogador (opcional)
        elif hab == "Nevasca" and j.mana >= 25:
            dano = random.randint(25, 35); j.mana -= 25; m.vida = max(0, m.vida - dano)
        elif hab == "Cura Congelada" and j.mana >= 20:
            cura = 20; j.mana -= 20; j.vida = min(j.vida + cura, j.vida_max)
    else:
        # Tipo 3 ou raios
        if hab == "Raio Elétrico" and j.mana >= 15:
            dano = random.randint(14, 20); j.mana -= 15; m.vida = max(0, m.vida - dano)
        elif hab == "Tempestade" and j.mana >= 25:
            dano = random.randint(25, 35); j.mana -= 25; m.vida = max(0, m.vida - dano)
        elif hab == "Cura Estática" and j.mana >= 20:
            cura = 20; j.mana -= 20; j.vida = min(j.vida + cura, j.vida_max)

# ---------------- ATIRADOR ----------------
def _habilidades_atirador(j, m, hab):
    if hab == "Tiro Certeiro" and getattr(j, "energia", 0) >= 10:
        dano = random.randint(15, 25); j.energia -= 10; m.vida = max(0, m.vida - dano)
    elif hab == "Disparo Duplo" and getattr(j, "energia", 0) >= 8:
        dano = random.randint(10, 18); j.energia -= 8; m.vida = max(0, m.vida - dano)
    elif hab == "Foco" and getattr(j, "energia", 0) >= 5:
        j.energia = min(getattr(j, "energia", 0) + 10, 60)
        j.energia -= 5  # custo
    else:
        pass

# ---------------- BARDO ----------------
def _habilidades_bardo(j, m, hab):
    if hab == "Melodia Afiada" and getattr(j, "mana", 0) >= 10:
        dano = random.randint(10, 20); j.mana -= 10; m.vida = max(0, m.vida - dano)
    elif hab == "Canção Inspiradora" and getattr(j, "mana", 0) >= 15:
        cura = 20; j.mana -= 15; j.vida = min(j.vida + cura, j.vida_max)
    elif hab == "Acorde Fatal" and getattr(j, "mana", 0) >= 20:
        dano = random.randint(20, 30); j.mana -= 20; m.vida = max(0, m.vida - dano)
    else:
        pass

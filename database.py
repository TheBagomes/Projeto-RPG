import sqlite3

DB_FILE = "rpg_game.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        classe TEXT NOT NULL,
        nivel INTEGER DEFAULT 1,
        vida INTEGER DEFAULT 100,
        vida_max INTEGER DEFAULT 100,
        ataque INTEGER DEFAULT 10,
        defesa INTEGER DEFAULT 5,
        energia INTEGER DEFAULT 0,
        mana INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def inserir_personagem(p):
    conn = get_connection()
    c = conn.cursor()
    energia = getattr(p, "energia", 0)
    mana = getattr(p, "mana", 0)
    c.execute("""
        INSERT INTO personagens (nome, classe, nivel, vida, vida_max, ataque, defesa, energia, mana)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (p.nome, p.classe, 1, p.vida, p.vida_max, p.ataque, p.defesa, energia, mana))
    conn.commit()
    conn.close()


def atualizar_personagem(p):
    conn = get_connection()
    c = conn.cursor()
    energia = getattr(p, "energia", 0)
    mana = getattr(p, "mana", 0)
    c.execute("""
        UPDATE personagens
        SET vida=?, ataque=?, defesa=?, energia=?, mana=?
        WHERE nome=? AND classe=?
    """, (p.vida, p.ataque, p.defesa, energia, mana, p.nome, p.classe))
    conn.commit()
    conn.close()

def listar_personagens():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM personagens")
    dados = c.fetchall()
    conn.close()
    return dados

def buscar_personagem(id_personagem):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM personagens WHERE id = ?", (id_personagem,))
    p = c.fetchone()
    conn.close()
    return p

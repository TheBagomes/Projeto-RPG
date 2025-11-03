# database.py
import sqlite3
from typing import List, Tuple

DB_FILE = "rpg_game.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # facilita leitura por nome de coluna, se desejar
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        classe TEXT NOT NULL,
        nivel INTEGER NOT NULL DEFAULT 1,
        vida INTEGER NOT NULL DEFAULT 100,
        mana INTEGER NOT NULL DEFAULT 50
    )
    """)
    conn.commit()
    conn.close()

def inserir_personagem(nome: str, classe: str, nivel: int = 1, vida: int = 100, mana: int = 50) -> int:
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    INSERT INTO personagens (nome, classe, nivel, vida, mana)
    VALUES (?, ?, ?, ?, ?)
    """, (nome, classe, nivel, vida, mana))
    conn.commit()
    last_id = c.lastrowid
    conn.close()
    return last_id

def listar_personagens() -> List[Tuple]:
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, nome, classe, nivel, vida, mana FROM personagens ORDER BY id")
    linhas = c.fetchall()
    conn.close()
    return linhas

def buscar_personagem_por_id(pid: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, nome, classe, nivel, vida, mana FROM personagens WHERE id = ?", (pid,))
    linha = c.fetchone()
    conn.close()
    return linha

def atualizar_personagem(pid: int, nivel: int, vida: int, mana: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    UPDATE personagens
    SET nivel = ?, vida = ?, mana = ?
    WHERE id = ?
    """, (nivel, vida, mana, pid))
    conn.commit()
    conn.close()

def deletar_personagem(pid: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM personagens WHERE id = ?", (pid,))
    conn.commit()
    conn.close()

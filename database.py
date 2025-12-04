import sqlite3

# ========================== CONEXÃO ==========================
class ConexaoDB:
    def __init__(self, nome="rpg.db"):
        self.nome = nome

    def conectar(self):
        conn = sqlite3.connect(self.nome)
        conn.row_factory = sqlite3.Row
        return conn

conexao = ConexaoDB()

# ========================== CRIAR TABELA ==========================
def criar_tabela():
    conn = conexao.conectar()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS personagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            classe TEXT NOT NULL,
            tipo TEXT,
            nivel INTEGER NOT NULL,
            vida INTEGER NOT NULL,
            vida_max INTEGER NOT NULL,
            ataque INTEGER NOT NULL,
            defesa INTEGER NOT NULL,
            energia INTEGER,
            mana INTEGER
        )
    """)

    conn.commit()
    conn.close()


# Cria a tabela automaticamente ao importar o módulo
criar_tabela()

# ========================== INSERIR ==========================
def inserir_personagem(p):
    tipo = getattr(p, "tipo", None)
    energia = getattr(p, "energia", None)
    mana = getattr(p, "mana", None)

    conn = conexao.conectar()
    c = conn.cursor()

    c.execute("""
        INSERT INTO personagens (nome, classe, tipo, nivel, vida, vida_max, ataque, defesa, energia, mana)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (p.nome, p.classe, tipo, 1, p.vida, p.vida_max, p.ataque, p.defesa, energia, mana))

    conn.commit()
    conn.close()

# ========================== BUSCAR PERSONAGEM ==========================
def buscar_personagem(pid):
    conn = conexao.conectar()
    c = conn.cursor()

    c.execute("SELECT * FROM personagens WHERE id = ?", (pid,))
    p = c.fetchone()

    conn.close()
    return p

# ========================== LISTAR ==========================
def listar_personagens():
    conn = conexao.conectar()
    c = conn.cursor()

    c.execute("SELECT * FROM personagens")
    dados = c.fetchall()

    conn.close()
    return dados

# ========================== CARREGAR ==========================
def carregar_personagem(pid):
    return buscar_personagem(pid)

# ========================== SALVAR ==========================
def salvar_personagem(p):
    conn = conexao.conectar()
    c = conn.cursor()

    energia = getattr(p, "energia", None)
    mana = getattr(p, "mana", None)
    tipo = getattr(p, "tipo", None)

    c.execute("""
        UPDATE personagens
        SET vida=?, vida_max=?, ataque=?, defesa=?, energia=?, mana=?, tipo=?, nivel=?
        WHERE id=?
    """, (p.vida, p.vida_max, p.ataque, p.defesa, energia, mana, tipo, p.nivel, p.id))

    conn.commit()
    conn.close()

# ========================== EXCLUIR ==========================
def excluir_personagem(pid):
    conn = conexao.conectar()
    c = conn.cursor()

    c.execute("DELETE FROM personagens WHERE id = ?", (pid,))
    conn.commit()
    conn.close()

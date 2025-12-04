import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import traceback

# Banco de dados 
from database import inserir_personagem, listar_personagens, buscar_personagem, salvar_personagem, excluir_personagem

try:
    from personagens.atirador import Atirador
    from personagens.bardo import Bardo
    from personagens.guerreiro import Guerreiro
    from personagens.magos import Magos
except Exception:

    class Guerreiro:
        def __init__(self, nome): 
            self.nome = nome; self.classe = "Guerreiro"; self.vida = 80; self.vida_max = 80; self.ataque = 10; self.defesa = 5; self.energia = 30
    class Magos:
        def __init__(self, nome):
            self.nome = nome; self.classe = "Magos"; self.tipo = "1"; self.vida = 60; self.vida_max = 60; self.ataque = 6; self.defesa = 3; self.mana = 40
    class Atirador:
        def __init__(self, nome):
            self.nome = nome; self.classe = "Atirador"; self.vida = 80; self.vida_max = 80; self.ataque = 10; self.defesa = 5; self.energia = 30
    class Bardo:
        def __init__(self, nome):
            self.nome = nome; self.classe = "Bardo"; self.vida = 60; self.vida_max = 60; self.ataque = 6; self.defesa = 3; self.mana = 40

# Import de monstros e habilidade 
try:
    from personagens.monstros import gerar_monstro
except Exception:
    def gerar_monstro():
        class M:
            def __init__(self):
                self.nome = "MonstroDummy"; self.vida = 30; self.vida_max = 30; self.ataque = 6
        return M()

try:
    from personagens.habilidades import usar_habilidade
except Exception:
    def usar_habilidade(jogador, monstro, habilidade):
        # Fallback: causa dano simples
        dano = random.randint(1, max(1, getattr(jogador, "ataque", 5)))
        monstro.vida = max(0, monstro.vida - dano)


# -----------------  habilidades  -----------------
def obter_habilidades_para(p):
    """Retorna listas de nomes de habilidades baseadas em classe/subtipo."""
    if not p or not hasattr(p, "classe"):
        return []
    if p.classe == "Guerreiro":
        return ["Golpe Poderoso", "Investida", "Recuperar Fôlego"]
    if p.classe == "Magos":
        tipo = getattr(p, "subtipo", getattr(p, "tipo", "1"))
        if tipo in ["1", "Fogo", "Mago de Fogo"]:
            return ["Bola de Fogo", "Chama Mística", "Cura Ígnea"]
        if tipo in ["2", "Gelo", "Mago de Gelo"]:
            return ["Lança de Gelo", "Nevasca", "Cura Congelada"]
        return ["Raio Elétrico", "Tempestade", "Cura Estática"]
    if p.classe == "Atirador":
        return ["Tiro Certeiro", "Disparo Duplo", "Foco"]
    if p.classe == "Bardo":
        return ["Melodia Afiada", "Canção Inspiradora", "Acorde Fatal"]
    return []

def reconstruir_personagem(row):
    """Transforma uma sqlite3.Row em um objeto de personagem das suas classes."""
    if row is None:
        return None
    try:
        classe = row["classe"]
    except Exception:
        try:
            classe = row["classe"]
        except Exception:
            return None

    nome = row["nome"]
    if classe == "Guerreiro":
        p = Guerreiro(nome)
    elif classe == "Magos":
        p = Magos(nome)
    elif classe == "Atirador":
        p = Atirador(nome)
    elif classe == "Bardo":
        p = Bardo(nome)
    else:
        p = Guerreiro(nome)

    # atualizar stats do banco de Dados 
    try:
        p.vida = row["vida"]
        p.vida_max = row["vida_max"]
        p.ataque = row["ataque"]
        p.defesa = row["defesa"]
    except Exception:
        try:
            p.vida = row[5]; p.vida_max = row[6]; p.ataque = row[7]; p.defesa = row[8]
        except Exception:
            pass

    # mana/energia
    if "mana" in row.keys() and hasattr(p, "mana"):
        p.mana = row["mana"]
    if "energia" in row.keys() and hasattr(p, "energia"):
        p.energia = row["energia"]

    # subtipo 
    tipo_val = row["tipo"] if "tipo" in row.keys() else None
    if tipo_val:
        p.subtipo = tipo_val
    else:
        p.subtipo = getattr(p, "tipo", "1")

    # id e nivel 
    if "id" in row.keys():
        p.id = row["id"]
    else:
        p.id = None
    p.nivel = row["nivel"] if "nivel" in row.keys() else getattr(p, "nivel", 1)

    # habilidades
    p.habilidades = obter_habilidades_para(p)
    return p


# ----------------- GUI principal -----------------
class RPGGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RPG - Interface")
        self.geometry("900x520")
        self.resizable(False, False)
        try:
            style = ttk.Style(self)
            style.theme_use("clam")
        except Exception:
            pass

        self.configure(bg="#1f1f2e")

        self.personagem = None
        self.monstro = None

        self.main_frame = ttk.Frame(self)
        self.main_frame.place(relwidth=1, relheight=1)
        self.log = None
        self.menu_inicial()

    def clear_frame(self):
        for w in self.main_frame.winfo_children():
            w.destroy()

    def append_log(self, text):
        if not self.log:
            return
        self.log.configure(state="normal")
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)
        self.log.configure(state="disabled")

    # ---------------- MENU INICIAL ----------------
    def menu_inicial(self):
        self.clear_frame()
        head = tk.Label(self.main_frame, text="RPG - Menu Inicial", font=("Segoe UI", 22, "bold"),
                        bg="#1f1f2e", fg="white")
        head.pack(pady=20)

        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Novo Jogo", width=20, command=self.tela_criar_personagem).grid(row=0, column=0, pady=6, padx=6)
        ttk.Button(btn_frame, text="Carregar Jogo", width=20, command=self.tela_carregar).grid(row=1, column=0, pady=6, padx=6)
        ttk.Button(btn_frame, text="Sair", width=20, command=self.quit).grid(row=2, column=0, pady=6, padx=6)

    # ---------------- CRIAR PERSONAGEM ----------------
    def tela_criar_personagem(self):
        self.clear_frame()
        title = tk.Label(self.main_frame, text="Criar Personagem", font=("Segoe UI", 18, "bold"),
                         bg="#1f1f2e", fg="white")
        title.pack(pady=12)

        form = ttk.Frame(self.main_frame)
        form.pack(pady=8)

        ttk.Label(form, text="Nome:").grid(row=0, column=0, sticky="w")
        nome_entry = ttk.Entry(form, width=30)
        nome_entry.grid(row=0, column=1, padx=6, pady=6)

        ttk.Label(form, text="Classe:").grid(row=1, column=0, sticky="w")
        classe_box = ttk.Combobox(form, values=["Guerreiro", "Magos", "Atirador", "Bardo"], state="readonly")
        classe_box.grid(row=1, column=1, padx=6, pady=6)
        classe_box.current(0)

        ttk.Label(form, text="Subclasse:").grid(row=2, column=0, sticky="w")
        sub_box = ttk.Combobox(form, values=[], state="readonly")
        sub_box.grid(row=2, column=1, padx=6, pady=6)

        preview = tk.Label(self.main_frame, text="", bg="#1f1f2e", fg="white", font=("Segoe UI", 10))
        preview.pack(pady=6)

        def atualizar_preview(event=None):
            c = classe_box.get()
            tmp = None
            if c == "Guerreiro": tmp = Guerreiro("tmp")
            elif c == "Magos": tmp = Magos("tmp")
            elif c == "Atirador": tmp = Atirador("tmp")
            elif c == "Bardo": tmp = Bardo("tmp")
            if tmp:
                text = f"Vida: {tmp.vida}/{tmp.vida_max}   Ataque: {tmp.ataque}   Defesa: {tmp.defesa}"
                if hasattr(tmp, "mana"):
                    text += f"   Mana: {getattr(tmp, 'mana', 0)}"
                if hasattr(tmp, "energia"):
                    text += f"   Energia: {getattr(tmp, 'energia', 0)}"
                preview.config(text=text)

            # atualizar opções de subclasse
            subs = []
            if c == "Guerreiro":
                subs = ["Tank", "Lutador"]
            elif c == "Magos":
                subs = ["Mago de Fogo", "Mago de Gelo", "Mago de Raio"]
            elif c == "Atirador":
                subs = ["Arqueiro", "Lançador"]
            elif c == "Bardo":
                subs = ["Virtuoso", "Harpista"]
            sub_box["values"] = subs
            if subs:
                sub_box.current(0)

        classe_box.bind("<<ComboboxSelected>>", atualizar_preview)
        atualizar_preview()

        def criar():
            nome = nome_entry.get().strip()
            classe = classe_box.get()
            subtipo = sub_box.get()
            if not nome:
                messagebox.showerror("Erro", "Digite um nome para o personagem.")
                return

            if classe == "Guerreiro": p = Guerreiro(nome)
            elif classe == "Magos": p = Magos(nome)
            elif classe == "Atirador": p = Atirador(nome)
            elif classe == "Bardo": p = Bardo(nome)
            else:
                messagebox.showerror("Erro", "Classe inválida.")
                return

            # armazenar subtipo e habilidades
            p.subtipo = subtipo
            p.habilidades = obter_habilidades_para(p)

            try:
                inserir_personagem(p)
            except Exception:
                traceback.print_exc()
                messagebox.showerror("Erro", "Falha ao salvar no banco. Veja console.")
                return
            
            # listar e achar último inserido com mesmo nome/classe 
            try:
                rows = listar_personagens()
             
                for r in reversed(rows):
                    if r["nome"] == p.nome and r["classe"] == p.classe:
                        p.id = r["id"]
                        break
            except Exception:
                p.id = None

            self.personagem = p
            messagebox.showinfo("Sucesso", f"{p.nome} ({p.classe} - {p.subtipo}) criado e salvo.")
            self.menu_personagem()

        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=8)
        ttk.Button(btn_frame, text="Criar", command=criar).grid(row=0, column=0, padx=6)
        ttk.Button(btn_frame, text="Voltar", command=self.menu_inicial).grid(row=0, column=1, padx=6)

    # ---------------- TELA CARREGAR (com excluir) ----------------
    def tela_carregar(self):
        self.clear_frame()
        title = tk.Label(self.main_frame, text="Carregar Personagem", font=("Segoe UI", 18, "bold"),
                         bg="#1f1f2e", fg="white")
        title.pack(pady=12)

        try:
            lista = listar_personagens()
        except Exception:
            traceback.print_exc()
            messagebox.showerror("Erro", "Falha ao listar personagens do banco.")
            lista = []

        if not lista:
            ttk.Label(self.main_frame, text="Nenhum personagem salvo.", background="#1f1f2e", foreground="white").pack(pady=10)
            ttk.Button(self.main_frame, text="Voltar", command=self.menu_inicial).pack(pady=6)
            return

        lb = tk.Listbox(self.main_frame, width=60, height=10)
        ids = []
        for r in lista:
            tipo = r["tipo"] if "tipo" in r.keys() else ""
            lb.insert(tk.END, f"[{r['id']}] {r['nome']} - {r['classe']} {tipo}")
            ids.append(r["id"])
        lb.pack(pady=8)

        def carregar_sel():
            sel = lb.curselection()
            if not sel:
                messagebox.showerror("Erro", "Selecione um personagem.")
                return
            idx = sel[0]
            pid = ids[idx]
            try:
                row = buscar_personagem(pid)
                self.personagem = reconstruir_personagem(row)
                messagebox.showinfo("Carregado", f"{self.personagem.nome} carregado.")
                self.menu_personagem()
            except Exception:
                traceback.print_exc()
                messagebox.showerror("Erro", "Falha ao carregar personagem.")

        def excluir_sel():
            sel = lb.curselection()
            if not sel:
                messagebox.showerror("Erro", "Selecione um personagem.")
                return
            idx = sel[0]
            pid = ids[idx]
            resp = messagebox.askyesno("Excluir", "Tem certeza que deseja excluir este personagem?")
            if resp:
                try:
                    excluir_personagem(pid)
                    messagebox.showinfo("Excluído", "Personagem removido do banco.")
                    self.tela_carregar()
                except Exception:
                    traceback.print_exc()
                    messagebox.showerror("Erro", "Falha ao excluir personagem.")

        btns = ttk.Frame(self.main_frame)
        btns.pack(pady=6)
        ttk.Button(btns, text="Carregar", command=carregar_sel).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Excluir", command=excluir_sel).grid(row=0, column=1, padx=6)
        ttk.Button(btns, text="Voltar", command=self.menu_inicial).grid(row=0, column=2, padx=6)

    # ---------------- MENU DO PERSONAGEM ----------------
    def menu_personagem(self):
        self.clear_frame()
        p = self.personagem
        if not p:
            messagebox.showerror("Erro", "Nenhum personagem carregado.")
            return

        head = tk.Label(self.main_frame, text=f"{p.nome} - {p.classe}", font=("Segoe UI", 18, "bold"), bg="#1f1f2e", fg="white")
        head.pack(pady=10)

        info = f"Vida: {p.vida}/{p.vida_max}   Ataque: {p.ataque}   Defesa: {p.defesa}"
        if hasattr(p, "mana"):
            info += f"   Mana: {p.mana}"
        if hasattr(p, "energia"):
            info += f"   Energia: {p.energia}"
        if hasattr(p, "subtipo"):
            info += f"   Subclasse: {p.subtipo}"

        tk.Label(self.main_frame, text=info, bg="#1f1f2e", fg="white", font=("Segoe UI", 11)).pack(pady=6)

        btns = ttk.Frame(self.main_frame)
        btns.pack(pady=8)
        ttk.Button(btns, text="Status", command=lambda: self.tela_status(self.personagem)).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Iniciar Batalha", command=self.tela_batalha).grid(row=0, column=1, padx=6)
        ttk.Button(btns, text="Salvar e Voltar ao Menu", command=self.salvar_e_voltar).grid(row=0, column=2, padx=6)

    def salvar_e_voltar(self):
        if self.personagem:
            try:
                # salvar_personagem espera que objeto tenha .id para WHERE id=?
                if not hasattr(self.personagem, "id") or self.personagem.id is None:
                    # tente inserir novamente
                    inserir_personagem(self.personagem)
                    # atualizar id
                    rows = listar_personagens()
                    for r in reversed(rows):
                        if r["nome"] == self.personagem.nome and r["classe"] == self.personagem.classe:
                            self.personagem.id = r["id"]
                            break
                else:
                    salvar_personagem(self.personagem)
                messagebox.showinfo("Salvo", "Personagem salvo no banco.")
            except Exception:
                traceback.print_exc()
                messagebox.showerror("Erro", "Falha ao salvar personagem.")
        self.menu_inicial()

    # ---------------- TELA STATUS ----------------
    def tela_status(self, personagem):
        self.clear_frame()
        title = tk.Label(self.main_frame, text=f"Status de {personagem.nome}", font=("Segoe UI", 18, "bold"), bg="#1f1f2e", fg="white")
        title.pack(pady=10)

        texto = f"Classe: {personagem.classe}\nVida: {personagem.vida}/{personagem.vida_max}\nAtaque: {personagem.ataque}\nDefesa: {personagem.defesa}"
        if hasattr(personagem, "mana"):
            texto += f"\nMana: {personagem.mana}"
        if hasattr(personagem, "energia"):
            texto += f"\nEnergia: {personagem.energia}"
        if hasattr(personagem, "subtipo"):
            texto += f"\nSubclasse: {personagem.subtipo}"

        ttk.Label(self.main_frame, text=texto, background="#1f1f2e", foreground="white", font=("Segoe UI", 12)).pack(pady=8)
        ttk.Button(self.main_frame, text="Voltar", command=self.menu_personagem).pack(pady=6)

    # ---------------- TELA DE BATALHA ----------------
    def tela_batalha(self):
        if not self.personagem:
            messagebox.showerror("Erro", "Nenhum personagem carregado.")
            return

        self.clear_frame()
        self.monstro = gerar_monstro()

        left = ttk.Frame(self.main_frame, width=260)
        left.pack(side="left", fill="y", padx=8, pady=8)
        mid = ttk.Frame(self.main_frame, width=380)
        mid.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        right = ttk.Frame(self.main_frame, width=260)
        right.pack(side="left", fill="y", padx=8, pady=8)

        # Player info (Esquerda)
        tk.Label(left, text=f"{self.personagem.nome}", font=("Segoe UI", 14, "bold"), bg="#1f1f2e", fg="white").pack(pady=6)
        self.lbl_p_vida = tk.Label(left, text=f"Vida: {self.personagem.vida}/{self.personagem.vida_max}", bg="#1f1f2e", fg="white")
        self.lbl_p_vida.pack(pady=4)
        self.lbl_p_stats = tk.Label(left, text=f"Ataque: {self.personagem.ataque}  Defesa: {self.personagem.defesa}", bg="#1f1f2e", fg="white")
        self.lbl_p_stats.pack(pady=4)
        if hasattr(self.personagem, "mana"):
            self.lbl_p_mana = tk.Label(left, text=f"Mana: {self.personagem.mana}", bg="#1f1f2e", fg="white")
            self.lbl_p_mana.pack(pady=4)
        if hasattr(self.personagem, "energia"):
            self.lbl_p_energia = tk.Label(left, text=f"Energia: {self.personagem.energia}", bg="#1f1f2e", fg="white")
            self.lbl_p_energia.pack(pady=4)

        # Monstro info (Direita)
        tk.Label(right, text=f"{self.monstro.nome}", font=("Segoe UI", 14, "bold"), bg="#1f1f2e", fg="white").pack(pady=6)
        self.lbl_m_vida = tk.Label(right, text=f"Vida: {self.monstro.vida}/{self.monstro.vida_max}", bg="#1f1f2e", fg="white")
        self.lbl_m_vida.pack(pady=4)
        self.lbl_m_stats = tk.Label(right, text=f"Ataque: {getattr(self.monstro,'ataque',0)}", bg="#1f1f2e", fg="white")
        self.lbl_m_stats.pack(pady=4)

        # Log central 
        self.log = scrolledtext.ScrolledText(mid, width=46, height=18, state="disabled", wrap="word", font=("Consolas", 10))
        self.log.pack(pady=4)

        # Ações
        actions = ttk.Frame(mid)
        actions.pack(pady=6)
        ttk.Button(actions, text="Atacar (1d20)", command=self.action_atacar).grid(row=0, column=0, padx=6)
        ttk.Button(actions, text="Usar Habilidade", command=self.action_habilidade).grid(row=0, column=1, padx=6)
        ttk.Button(actions, text="Fugir", command=self.action_fugir).grid(row=0, column=2, padx=6)

        # iniciar log
        self.append_log(f"!!! BATALHA: {self.personagem.nome} VS {self.monstro.nome} !!!")
        self.append_log(f"Vida Jogador: {self.personagem.vida}   Vida Monstro: {self.monstro.vida}")

        ttk.Button(self.main_frame, text="Salvar Personagem", command=lambda: salvar_personagem(self.personagem)).place(x=10, y=480)

    # ---------------- AÇÕES DE BATALHA ----------------
    def action_atacar(self):
        rolagem_j = random.randint(1, 20)
        rolagem_m = random.randint(1, 20)
        self.append_log(f"{self.personagem.nome} rolou {rolagem_j}")
        self.append_log(f"{self.monstro.nome} rolou {rolagem_m}")

        if rolagem_j > rolagem_m:
            dano = random.randint(1, max(1, self.personagem.ataque))
            self.monstro.vida = max(0, self.monstro.vida - dano)
            self.append_log(f"{self.personagem.nome} acertou e causou {dano} de dano! ({self.monstro.vida}/{self.monstro.vida_max})")
        elif rolagem_m > rolagem_j:
            dano = random.randint(1, max(1, getattr(self.monstro, "ataque", 5)))
            self.personagem.vida = max(0, self.personagem.vida - dano)
            self.append_log(f"{self.monstro.nome} atacou e causou {dano} de dano! ({self.personagem.vida}/{self.personagem.vida_max})")
        else:
            self.append_log("Empate! Ninguém causa dano.")

        self.atualizar_labels()
        self.verificar_fim_turno()

    def action_habilidade(self):
        hab = self.escolher_habilidade_popup()
        if not hab:
            return

        self.append_log(f"{self.personagem.nome} tentou usar '{hab}'")
        rolagem_j = random.randint(1, 20)
        rolagem_m = random.randint(1, 20)
        self.append_log(f"Jogador rolou {rolagem_j}")
        self.append_log(f"Monstro rolou {rolagem_m}")

        if rolagem_j >= rolagem_m:
            try:
                usar_habilidade(self.personagem, self.monstro, hab)
                self.append_log(f"{self.personagem.nome} usou {hab}!")
            except Exception as e:
                traceback.print_exc()
                dano = random.randint(1, max(1, self.personagem.ataque))
                self.monstro.vida = max(0, self.monstro.vida - dano)
                self.append_log(f"Habilidade falhou; causou {dano} de dano (fallback). Erro:{e}")
        else:
            dano = random.randint(1, max(1, getattr(self.monstro, "ataque", 5)))
            self.personagem.vida = max(0, self.personagem.vida - dano)
            self.append_log(f"{self.monstro.nome} aproveitou e causou {dano} de dano!")

        self.atualizar_labels()
        self.verificar_fim_turno()

    def action_fugir(self):
        chance = random.random()
        if chance < 0.5:
            self.append_log(f"{self.personagem.nome} tentou fugir e teve sucesso!")
            try:
                if hasattr(self.personagem, "id") and self.personagem.id:
                    salvar_personagem(self.personagem)
                else:
                    inserir_personagem(self.personagem)
            except Exception:
                traceback.print_exc()
            messagebox.showinfo("Fugiu", "Você fugiu da batalha. Personagem salvo.")
            self.menu_personagem()
        else:
            self.append_log(f"{self.personagem.nome} tentou fugir e falhou! Monstro ataca.")
            dano = random.randint(1, max(1, getattr(self.monstro, "ataque", 5)))
            self.personagem.vida = max(0, self.personagem.vida - dano)
            self.atualizar_labels()
            self.verificar_fim_turno()

    def atualizar_labels(self):
        try:
            self.lbl_p_vida.config(text=f"Vida: {self.personagem.vida}/{self.personagem.vida_max}")
            if hasattr(self.personagem, "mana") and hasattr(self, "lbl_p_mana"):
                self.lbl_p_mana.config(text=f"Mana: {self.personagem.mana}")
            if hasattr(self.personagem, "energia") and hasattr(self, "lbl_p_energia"):
                self.lbl_p_energia.config(text=f"Energia: {self.personagem.energia}")
            self.lbl_m_vida.config(text=f"Vida: {self.monstro.vida}/{self.monstro.vida_max}")
        except Exception:
            pass

    def verificar_fim_turno(self):
        if self.monstro.vida <= 0:
            self.append_log(f"{self.personagem.nome} venceu {self.monstro.nome}!")
            try:
                if hasattr(self.personagem, "id") and self.personagem.id:
                    salvar_personagem(self.personagem)
                else:
                    inserir_personagem(self.personagem)
            except Exception:
                traceback.print_exc()
            messagebox.showinfo("Vitória", f"Você venceu {self.monstro.nome}! Personagem salvo.")
            self.menu_personagem()
        elif self.personagem.vida <= 0:
            self.append_log(f"{self.personagem.nome} foi derrotado...")
            try:
                if hasattr(self.personagem, "id") and self.personagem.id:
                    salvar_personagem(self.personagem)
                else:
                    inserir_personagem(self.personagem)
            except Exception:
                traceback.print_exc()
            messagebox.showinfo("Derrota", f"{self.personagem.nome} foi derrotado... Dados salvos.")
            self.menu_inicial()


# ---------- escolha de habilidade ----------
    def escolher_habilidade_popup(self):
        habilidades = getattr(self.personagem, "habilidades", None)
        if not habilidades:
            messagebox.showerror("Erro", "Seu personagem não possui habilidades definidas.")
            return None

        popup = tk.Toplevel(self)
        popup.title("Escolher Habilidade")
        popup.geometry("320x300")
        popup.resizable(False, False)

        tk.Label(popup, text="Escolha uma habilidade:", font=("Segoe UI", 12, "bold")).pack(pady=10)

        lb = tk.Listbox(popup, width=40, height=8)
        for h in habilidades:
            lb.insert(tk.END, h)
        lb.pack(pady=10)

        selected = {"value": None}

        def confirmar():
            sel = lb.curselection()
            if not sel:
                messagebox.showerror("Erro", "Selecione uma habilidade.")
                return
            selected["value"] = habilidades[sel[0]]
            popup.destroy()

        ttk.Button(popup, text="Usar", command=confirmar).pack(pady=10)
        popup.wait_window()
        return selected["value"]


# ----------------- run -----------------
if __name__ == "__main__":
    app = RPGGUI()
    app.mainloop()

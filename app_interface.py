import tkinter as tk
from tkinter import messagebox, ttk
from banco_dados import criar_tabela, adicionar_nota, deletar_nota, conectar
from calculo_notas import media

# Inicializa o banco\criar_tabela()

class AplicativoNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Notas")
        self.root.geometry("600x400")

        # Frame de entrada de dados
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Disciplina:").grid(row=0, column=0)
        self.disciplina_entry = tk.Entry(frame_top)
        self.disciplina_entry.grid(row=0, column=1)

        tk.Label(frame_top, text="Unidade 1:").grid(row=1, column=0)
        self.unidade1_entry = tk.Entry(frame_top)
        self.unidade1_entry.grid(row=1, column=1)

        tk.Label(frame_top, text="Unidade 2:").grid(row=2, column=0)
        self.unidade2_entry = tk.Entry(frame_top)
        self.unidade2_entry.grid(row=2, column=1)

        tk.Button(frame_top, text="Adicionar Nota", command=self.adicionar_nota).grid(row=3, columnspan=2, pady=5)

        # Tabela de notas
        self.tree = ttk.Treeview(self.root, columns=("ID", "Disciplina", "U1", "U2", "Resultado"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Disciplina", text="Disciplina")
        self.tree.heading("U1", text="Unidade 1")
        self.tree.heading("U2", text="Unidade 2")
        self.tree.heading("Resultado", text="Resultado")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Botão de deletar
        tk.Button(self.root, text="Deletar Nota Selecionada", command=self.deletar_nota).pack(pady=5)

        self.carregar_notas()

    def adicionar_nota(self):
        disciplina = self.disciplina_entry.get()
        try:
            unidade1 = float(self.unidade1_entry.get())
            unidade2 = float(self.unidade2_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Notas devem ser números.")
            return

        resultado = media(unidade1, unidade2)
        adicionar_nota(disciplina, unidade1, unidade2, resultado)
        messagebox.showinfo("Sucesso", "Nota adicionada!")
        self.limpar_campos()
        self.carregar_notas()

    def carregar_notas(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notas")
        for nota in cursor.fetchall():
            self.tree.insert("", tk.END, values=nota)
        conn.close()

    def deletar_nota(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atenção", "Nenhuma nota selecionada.")
            return

        item = self.tree.item(selected[0])
        id_nota = item['values'][0]
        deletar_nota(id_nota)
        messagebox.showinfo("Sucesso", "Nota deletada!")
        self.carregar_notas()

    def limpar_campos(self):
        self.disciplina_entry.delete(0, tk.END)
        self.unidade1_entry.delete(0, tk.END)
        self.unidade2_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = AplicativoNotas(root)
    root.mainloop()

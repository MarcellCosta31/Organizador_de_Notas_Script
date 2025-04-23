import sqlite3
from tabulate import tabulate
from calculo_notas import media

def conectar():
    return sqlite3.connect('meubanco.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disciplina TEXT,
        unidade1 REAL,
        unidade2 REAL,
        resultado TEXT
    )
    ''')
    conn.commit()
    conn.close()

def adicionar_nota(disciplina, unidade1, unidade2, resultado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notas (disciplina, unidade1, unidade2, resultado)
        VALUES (?, ?, ?, ?)
    """, (disciplina, unidade1, unidade2, resultado))
    conn.commit()
    conn.close()

def deletar_nota(id_nota):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notas WHERE id = ?", (id_nota,))
    conn.commit()
    conn.close()

def editar_nota(id_nota, disciplina, unidade1, unidade2, resultado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE notas
        SET disciplina = ?, unidade1 = ?, unidade2 = ?, resultado = ?
        WHERE id = ?
    """, (disciplina, unidade1, unidade2, resultado, id_nota))
    conn.commit()
    conn.close()

def mostrar_notas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    conn.close()
    if notas:
        headers = ["Disciplina", "Unidade 1", "Unidade 2", "Resultado"]
        print("\nLista de notas:")
        print(tabulate(notas, headers=headers, tablefmt="fancy_grid"))
    else:
        print("\nNenhuma nota encontrada.")

def main():
    criar_tabela()
    while True:
        print("\n1. Adicionar nota")
        print("2. Deletar nota")
        print("3. Mostrar notas")
        print("4. Editar")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            disciplina = input("Disciplina: ")
            unidade1 = float(input("Nota da Unidade 1: "))
            unidade2 = float(input("Nota da Unidade 2: "))
            resultado = media(unidade1, unidade2)
            """resultado = input("Resultado (Aprovado/Reprovado): ")"""

            adicionar_nota(disciplina, unidade1, unidade2, resultado)
            print("Nota adicionada com sucesso!")

        elif escolha == "2":
            id_nota = int(input("ID da nota a deletar: "))
            deletar_nota(id_nota)
            print("Nota deletada com sucesso!")

        elif escolha == "3":
            mostrar_notas()

        elif escolha == "4":
            id_nota = int(input("ID da nota a editar: "))
            disciplina = input("Nova disciplina: ")
            unidade1 = float(input("Nova nota da Unidade 1: "))
            unidade2 = float(input("Nova nota da Unidade 2: "))
            resultado = media(unidade1, unidade2)
            editar_nota(id_nota, disciplina, unidade1, unidade2, resultado)
            print("Nota atualizada com sucesso!")

        elif escolha == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

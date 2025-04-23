from flask import Flask, render_template, request, redirect, url_for
from banco_dados import criar_tabela, adicionar_nota, deletar_nota, editar_nota, conectar
from calculo_notas import media

app = Flask(__name__)
criar_tabela()

@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    conn.close()
    return render_template('index.html', notas=notas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    disciplina = request.form['disciplina']
    unidade1 = float(request.form['unidade1'])
    unidade2 = float(request.form['unidade2'])
    resultado = media(unidade1, unidade2)
    adicionar_nota(disciplina, unidade1, unidade2, resultado)
    return redirect(url_for('index'))

@app.route('/editar/<int:id_nota>', methods=['POST'])
def editar(id_nota):
    disciplina = request.form['disciplina']
    unidade1 = float(request.form['unidade1'])
    unidade2 = float(request.form['unidade2'])
    resultado = media(unidade1, unidade2)
    editar_nota(id_nota, disciplina, unidade1, unidade2, resultado)
    return redirect(url_for('index'))

@app.route('/deletar/<int:id_nota>')
def deletar(id_nota):
    deletar_nota(id_nota)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

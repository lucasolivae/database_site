from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string

app = Flask(__name__)

# --------------------
# BANCO
# --------------------
def conectar():
    return sqlite3.connect("database.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id TEXT PRIMARY KEY,
            nome TEXT,
            nascimento TEXT,
            telefone TEXT
        )
    """)

    conn.commit()
    conn.close()

criar_tabela()

# --------------------
# GERAR ID
# --------------------
def gerar_id():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=6))

# --------------------
# ROTAS
# --------------------

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        nome = request.form["nome"]
        nascimento = request.form["nascimento"]
        telefone = request.form["telefone"]

        id_cliente = gerar_id()

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO clientes VALUES (?, ?, ?, ?)
        """, (id_cliente, nome, nascimento, telefone))

        conn.commit()
        conn.close()

        return redirect("/")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM clientes")
    clientes = cursor.fetchall()

    conn.close()

    return render_template("index.html", clientes=clientes)


@app.route("/cliente/<id>")
def cliente(id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM clientes WHERE id = ?
    """, (id,))

    cliente = cursor.fetchone()

    conn.close()

    return render_template("cliente.html", cliente=cliente)


@app.route("/buscar", methods=["POST"])
def buscar():
    termo = request.form["termo"]

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM clientes
        WHERE id = ? OR nome LIKE ?
    """, (termo, f"%{termo}%"))

    clientes = cursor.fetchall()
    conn.close()

    return render_template("resultado.html", clientes=clientes)


if __name__ == "__main__":
    app.run(debug=True)

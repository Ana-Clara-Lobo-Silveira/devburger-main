from flask import Flask, render_template, request, redirect, session, flash
from model.produtos import rec_produtos_rap
from model.produtos import rec_destaques
from model.produtos import rec_produto_u
from model.cadastro import cadastro
from model.cadastro import verifica_cadastrado

app = Flask(__name__)
app.secret_key = "DevBurguer"

@app.route("/")
def pg_index():
    recuperar_destaques = rec_destaques()
    recuperar_produtos = rec_produtos_rap()
    if "usuario_log" not in session:
         return redirect("/login")
    else:
        return render_template("index.html", produtos = recuperar_produtos, destaques = recuperar_destaques)
@app.route("/produto/<codigo>")
def pg_produto(codigo):
    recuperar_produto = rec_produto_u(codigo)
    return render_template("produto.html", produto = recuperar_produto)
# -----------------------------------------------------------------------

@app.route("/cadastro", methods = ["GET"])
def pg_cadastro_get():
    return render_template("cadastro.html")

@app.route("/cadastro", methods = ["POST"])
def pg_cadastro():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")
    if cadastro(usuario, senha, nome):
        return redirect("/login")
    else:
        return "Complete as informações corretamente"
    
@app.route("/login", methods = ["GET"])
def pg_login_get():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def pg_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    usuario_log_s= verifica_cadastrado(usuario,senha)

    if usuario_log_s:
        session["usuario_log"] = usuario_log_s["nome"]
        return redirect("/")
    else:
        return redirect("/login")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
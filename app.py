from flask import Flask, render_template
from model.produtos import rec_produtos_rap
from model.produtos import rec_destaques
from model.produtos import rec_produto_u

app = Flask(__name__)


@app.route("/")
def pg_index():
    recuperar_destaques = rec_destaques()
    recuperar_produtos = rec_produtos_rap()
    return render_template("index.html", produtos = recuperar_produtos, destaques = recuperar_destaques)

@app.route("/produto/<codigo>")
def pg_produto(codigo):
    recuperar_produto = rec_produto_u(codigo)
    return render_template("produto.html", produto = recuperar_produto)


if __name__ == "__main__":
    app.run(debug=True)
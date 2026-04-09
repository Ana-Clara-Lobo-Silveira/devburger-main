from flask import Flask, render_template
from model.produtos import rec_produtos
from model.produtos import rec_destaques

app = Flask(__name__)


@app.route("/")
def pg_index():
    recuperar_produtos = rec_produtos()
    recuperar_destaques = rec_destaques()
    return render_template("index.html", produto = recuperar_produtos, destaques = recuperar_destaques)

@app.route("/produto")
def pg_produto():
    return render_template("produto.html")


if __name__ == "__main__":
    app.run(debug=True)
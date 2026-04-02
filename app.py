from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def pg_index():
    return render_template("index.html")

@app.route("/produto")
def pg_produto():
    return render_template("produto.html")


if __name__ == "__main__":
    app.run(debug=True)
from database.conexao import Conexao

def rec_destaques():
    con, cur  = Conexao.conectar()
    cur.execute("SELECT  destaque, url_imagem FROM produto where destaque  = 1;")
    destaques = cur.fetchall()
    con.close()

    return destaques

def rec_produtos_rap():
    con, cur  = Conexao.conectar()
    cur.execute("SELECT url_imagem, produto, descricao, destaque, preco FROM produto;")
    produtos = cur.fetchall()
    con.close()

    return produtos

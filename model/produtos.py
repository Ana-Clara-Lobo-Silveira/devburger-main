from database.conexao import Conexao

def rec_produtos():
    con, cur  = Conexao.conectar()
    cur.execute("SELECT produto, descricao, destaque, preco, url_imagem FROM produto;")
    produtos = cur.fetchall()
    con.close()

    return produtos

def rec_destaques():
    con, cur  = Conexao.conectar()
    cur.execute("SELECT produto, descricao, preco, url_imagem FROM produto where destaque  = 1;")
    destaques = cur.fetchall()
    con.close()

    return destaques

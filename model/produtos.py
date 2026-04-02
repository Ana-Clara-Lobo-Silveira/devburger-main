from database.conexao import Conexao

def rec_produtos():
    con, cur  = Conexao.conectar()
    cur.execute("SELECT produto, descricao, detaque, preco FROM produto;")
    produtos = cur.fetchall()
    con.close()

    return produtos
from database.conexao import Conexao

def rec_carrinho(usuario:str)->list:
    con, cur  = Conexao.conectar()
    cur.execute("SELECT  codigo, destaque, url_imagem FROM produto where destaque  = 1;")
    resultado = cur.fetchall()
    con.close()

    return resultado

from database.conexao import Conexao

def cadastro(usuario:str, senha:str,nome:str=None):
    try:
        con, cur  = Conexao.conectar()
        cur.execute("INSERT INTO cadastro (usuario, senha, nome) VALUES (%s, %s, %s)", [usuario, senha, nome])
        con.commit()
        con.close()

        return True
    except Exception as erro:
        print(erro)
        return False
    
def verifica_cadastrado(usuario:str, senha:str) -> list:
        """Verifica o cadastro do usuário, caso esteja cadastrado retorna todos os dados, ao contrário retorbna "None"."""
        con, cur  = Conexao.conectar()
        cur.execute("SELECT nome FROM cadastro WHERE  usuario = %s AND senha=%s", [usuario, senha])
        g_usuario = cur.fetchone()
        con.close()

        return g_usuario
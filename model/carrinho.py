from database.conexao import Conexao

def rec_carrinho(usuario:str)->list:
    con, cur  = Conexao.conectar()
    cur.execute("""SELECT carrinho.codigo_carrinho,
                        carrinho.usuario,
                        carrinho.data,
                        carrinho.ped_fin,
                        produto.produto,
                        itens_car.quantidade,
                        produto.preco,
                        produto.url_imagem
                    FROM carrinho
                    INNER JOIN itens_car ON carrinho.codigo_carrinho = itens_car.codigo_carrinho
                    INNER JOIN produto ON produto.codigo = itens_car.codigo_produto
                    WHERE carrinho.usuario = %s;""", [usuario])
    resultado = cur.fetchall()
    con.close()

    return resultado

def ins_carrinho(usuario, codigo_produto, quantidade = 1):
    con, cur  = Conexao.conectar()
    cur.execute("""
                SELECT codigo_carrinho from carrinho
                WHERE usuario = %s and ped_fin = 0 limit 1;
                """, [usuario])
    ret_cod_carrinho = cur.fetchone()

    if ret_cod_carrinho:
        codigo_car = ret_cod_carrinho["codigo_carrinho"]
    else:
        cur.execute("INSERT INTO carrinho (usuario) VALUES (%s)", [usuario])
        codigo_car = cur.lastrowid

    cur.execute("INSERT INTO itens_car (codigo_carrinho, codigo_produto, quantidade) VALUES (%s, %s, %s)", [codigo_car, codigo_produto, quantidade])
    con.commit()
    con.close()


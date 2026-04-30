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

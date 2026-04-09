import mysql.connector

class Conexao():

    # transforma em metodo estático, só precisa chama-lo
    @staticmethod
    def conectar():
        con = mysql.connector.connect(
            host="localhost",
            port = 3306,
            user = "root",
            password="root",
            database = "cardapio"
        )
        cur = con.cursor(dictionary=True)

        return con, cur
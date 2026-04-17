create database cardapio;
use cardapio;

CREATE TABLE IF NOT EXISTS produto (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 produto VARCHAR(50),
 descricao VARCHAR(200),
 destaque bool,
 preco float,
 url_imagem VARCHAR(255),
 disponibilidade bool
);

CREATE TABLE IF NOT EXISTS cadastro(
usuario VARCHAR(20) NOT NULL PRIMARY KEY,
senha VARCHAR(200) NOT NULL, 
nome varchar(100) default "Anônimo"
);


select * from cadastro;

select * from produto;

drop database cardapio;

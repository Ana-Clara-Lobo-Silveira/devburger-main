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

CREATE TABLE IF NOT EXISTS carrinho(
	codigo_carrinho int auto_increment primary key,
    usuario varchar(20), 
    data datetime default current_timestamp, 
    ped_fin bool default 0,
    constraint fk_carrinho_usuario foreign key (usuario) references cadastro(usuario));
    
CREATE TABLE IF NOT EXISTS itens_car(
	codigo_item_car int auto_increment primary key,
    codigo_carrinho int,
    codigo_produto int,
    quantidade int default 1,
    constraint fk_itens_car_car foreign key (codigo_carrinho) references carrinho(codigo_carrinho),
    constraint fk_itens_car_prod foreign key (codigo_produto) references produto(codigo)
);
    


-- select * from cadastro;
-- show tables from cardapio;
-- select * from produto;
-- select * from carrinho;
-- drop database cardapio;

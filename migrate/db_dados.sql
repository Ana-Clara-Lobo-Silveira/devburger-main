insert into cardapio.produto (produto, descricao, destaque, preco, url_imagem, disponibilidade)
values("Hamburguer 1", "blablabla", 1, 200, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",0),
("Hamburguer 2", "blablabla", 0, 200, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",0),
("Hamburguer 3", "blablabla", 1, 200, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",0),
("Hamburguer 4", "blablabla", 0, 200, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",0);


INSERT INTO cardapio.cadastro
(`usuario`,
`senha`,
`nome`)
VALUES
("Ana Clara", "1234", "Ana");

insert into cardapio.carrinho(
	usuario, 
    ped_fin
) values('Ana Clara', 1);
INSERT INTO cardapio.itens_car 
(codigo_item_car,
 codigo_carrinho,
 codigo_produto,
 quantidade)
 VALUES
 ('1',
 '1',
 '1',
 '1')
 ;
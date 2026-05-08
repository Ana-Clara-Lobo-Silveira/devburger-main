insert into cardapio.produto (produto, descricao, destaque, preco, url_imagem, disponibilidade)
values("Hamburguer 1", "blablabla", 1, 200, "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",0),
("Hamburguer 2", "blablabla", 0, 200, "https://supermercadosrondon.com.br/guiadecarnes/images/postagens/quer_fazer_hamburger_artesanal_perfeito_2019-05-14.jpg",0),
("Hamburguer 3", "blablabla", 1, 200, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGO3xVrtBQpRvhtEzjuZL4IDjNFX88gWLoEA&s",0),
("Hamburguer 4", "blablabla", 0, 200, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK66J0zhU_ptRAYyNrsKD7u59X6h55kG_w_A&s",0);


INSERT INTO cardapio.cadastro
(`usuario`,
`senha`,
`nome`)
VALUES
("Ana Clara", "1234", "Ana"), ("Julia", "1234", "Ju");

insert into cardapio.carrinho(
	usuario, 
    ped_fin
) values('Ana Clara', 1);
-- INSERT INTO cardapio.itens_car 
-- (codigo_item_car,
 -- codigo_carrinho,
 -- codigo_produto,
 -- quantidade)
 -- VALUES
 -- ('1',
 -- ' 1',
 -- '1',
--  '1')
 -- ;
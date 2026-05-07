async function inserirItemCarrinho(codigo_produto, quantidade){
    const reposta = await fetch("/api/post/item_carrinho", {method: "POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({"codigo_produto":codigo_produto, "quantidade":quantidade})})
}
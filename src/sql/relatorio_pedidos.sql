select p.codigo_pedido
     , p.data_pedido
     , c.nome as cliente
     , nvl(f.nome_fantasia, f.razao_social) as empresa
     , i.codigo_item_pedido as item_pedido
     , prd.descricao_produto as produto
     , i.quantidade
     , i.valor_unitario
     , (i.quantidade * i.valor_unitario) as valor_total
  from pedidos p
  inner join clientes c
  on p.cpf = c.cpf
  inner join fornecedores f
  on p.cnpj = f.cnpj
  left join itens_pedido i
  on p.codigo_pedido = i.codigo_pedido
  left join produtos prd
  on i.codigo_produto = prd.codigo_produto
  order by c.nome, i.codigo_item_pedido
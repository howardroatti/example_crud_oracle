select i.codigo_pedido
     , i.codigo_item_pedido
     , i.codigo_produto
     , prd.descricao_produto
     , i.quantidade
     , i.valor_unitario
     , (i.quantidade * i.valor_unitario) as valor_total
  from itens_pedido i
  inner join produtos prd
  on i.codigo_produto = prd.codigo_produto
  order by i.codigo_pedido, prd.descricao_produto
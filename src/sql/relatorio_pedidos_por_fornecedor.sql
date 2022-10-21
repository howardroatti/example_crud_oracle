with sumariza_pedidos as (
    select cnpj
         , count(1) as qtd_pedidos
      from pedidos
      group by cnpj
)

select nvl(f.nome_fantasia, f.razao_social) as empresa
     , sp.qtd_pedidos
     , sum(i.quantidade * i.valor_unitario) as valor_total
  from pedidos p
  inner join sumariza_pedidos sp
  on p.cnpj = sp.cnpj
  inner join fornecedores f
  on p.cnpj = f.cnpj
  inner join itens_pedido i
  on p.codigo_pedido = i.codigo_pedido
  group by sp.qtd_pedidos, nvl(f.nome_fantasia, f.razao_social)
  order by nvl(f.nome_fantasia, f.razao_social)
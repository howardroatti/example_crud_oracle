select f.cnpj
       , f.razao_social
       , f.nome_fantasia
  from fornecedores f
 order by f.nome_fantasia
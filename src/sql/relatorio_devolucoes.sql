select devol.id_devolucao
     , devol.id_emprestimo 
     , devol.data_devolucao
  from devolucoes devol
 order by devol.id_devolucao
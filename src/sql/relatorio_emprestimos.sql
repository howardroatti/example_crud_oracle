select empr.id_emprestimo
     , empr.id_livro 
     , empr.id_usuario 
     , empr.data_emprestimo
     , empr.data_devolucao_sugerida
  from emprestimos empr
 order by empr.id_emprestimo
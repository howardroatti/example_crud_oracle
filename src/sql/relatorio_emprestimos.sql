select empr.id_emprestimo as "ID Emprestimo"
     , empr.id_livro as "ID Livro"
     , empr.id_usuario as "ID Usuario"
     , empr.data_emprestimo as "Data Emprestimo"
     , empr.data_devolucao_sugerida as "Devolucao Sugerida"
     , usu.nome as "Nome Usuario"
     , liv.titulo as "Titulo Livro"
  from emprestimos empr
  inner join livros liv on empr.id_livro = liv.id_livro
  inner join usuarios usu on empr.id_usuario = usu.id_usuario
 order by empr.id_emprestimo
SELECT
   empr.id_emprestimo AS "ID Emprestimo",
   empr.id_livro AS "ID Livro",
   empr.id_usuario AS "ID Usuario",
   empr.data_emprestimo AS "Data Emprestimo",
   empr.data_devolucao_sugerida AS "Devolucao Sugerida",
   usu.nome AS "Nome Usuario",
   liv.titulo AS "Titulo Livro",
   CASE 
      WHEN 
         EXISTS (
            SELECT
               1
            FROM
               devolucoes devo
            WHERE
               devo.id_emprestimo = empr.id_emprestimo
         )
      THEN 'Devolvido'
      ELSE 'Pendente'
   END as devolucao_realizada
FROM
   emprestimos empr
   INNER JOIN livros liv ON empr.id_livro = liv.id_livro
   INNER JOIN usuarios usu ON empr.id_usuario = usu.id_usuario
ORDER BY
   devolucao_realizada,
   empr.id_emprestimo
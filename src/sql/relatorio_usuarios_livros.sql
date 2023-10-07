SELECT
  usuario.id_usuario,
  usuario.nome,
  usuario.email,
  usuario.telefone,
   (
      SELECT
         COUNT(*)
      FROM
         emprestimos
      WHERE
         emprestimos.id_usuario = usuario.id_usuario
      AND
         emprestimos.id_emprestimo NOT IN (
         SELECT
            devolucoes.id_emprestimo
         FROM
            devolucoes
         )
   ) AS devolucoes_pendentes,
   (
      SELECT
         COUNT(*)
      FROM
         emprestimos
      WHERE
         emprestimos.id_usuario = usuario.id_usuario
   ) AS emprestimos_realizados
FROM
  usuarios usuario
ORDER BY 
  usuario.id_usuario

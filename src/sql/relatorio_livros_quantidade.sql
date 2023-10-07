SELECT
  livro.id_livro,
  livro.titulo,
  livro.autor,
  livro.ano_publicacao,
  livro.quantidade as quantidade_total,
  livro.quantidade - (
    SELECT
      COUNT(*)
    FROM
      emprestimos
    WHERE
      emprestimos.id_livro = livro.id_livro
    AND
      emprestimos.id_emprestimo NOT IN (
        SELECT
          devolucoes.id_emprestimo
        FROM
          devolucoes
      )
  ) AS disponibilidade
FROM
  livros livro
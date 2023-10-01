select livro.id_livro
     , livro.titulo 
     , livro.autor 
     , livro.ano_publicacao 
     , livro.quantidade 
     , livro.disponibilidade 
  from livros livro
 order by livro.id_livro
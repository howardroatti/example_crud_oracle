-- Inserindo valores iniciais na tabela "Livros"
INSERT INTO Livros (id_livro, titulo, autor, ano_publicacao, quantidade)
VALUES (LIVROS_ID_LIVRO_SEQ.NEXTVAL, 'Dom Casmurro', 'Machado de Assis', 1899, 1);

INSERT INTO Livros (id_livro, titulo, autor, ano_publicacao, quantidade)
VALUES (LIVROS_ID_LIVRO_SEQ.NEXTVAL, '1984', 'George Orwell', 1949, 1);

INSERT INTO Livros (id_livro, titulo, autor, ano_publicacao, quantidade)
VALUES (LIVROS_ID_LIVRO_SEQ.NEXTVAL, 'O Senhor dos Aneis', 'J.R.R. Tolkien', 1954, 1);

-- Inserindo valores iniciais na tabela "Usuarios"
INSERT INTO Usuarios (id_usuario, nome, email)
VALUES (USUARIOS_ID_USUARIO_SEQ.NEXTVAL, 'Joao Silva', 'joaosilva@gmail.com');

INSERT INTO Usuarios (id_usuario, nome, email, telefone)
VALUES (USUARIOS_ID_USUARIO_SEQ.NEXTVAL, 'Maria Souza', 'mariasouza@hotmail.com', '27999991234');

-- Inserindo valores iniciais na tabela "Emprestimos"
INSERT INTO Emprestimos (       id_emprestimo,  id_livro,       id_usuario,     data_emprestimo,                        data_devolucao_sugerida)
VALUES (EMPRESTIMOS_ID_EMPRESTIMO_SEQ.NEXTVAL,  1,              1,              TO_DATE('01/10/2023', 'DD/MM/YYYY'),    TO_DATE('15/10/2023', 'DD/MM/YYYY'));

INSERT INTO Emprestimos (       id_emprestimo,  id_livro,       id_usuario,     data_emprestimo,                        data_devolucao_sugerida)
VALUES (EMPRESTIMOS_ID_EMPRESTIMO_SEQ.NEXTVAL,  2,              2,              TO_DATE('25/09/2023', 'DD/MM/YYYY'),    TO_DATE('10/10/2023', 'DD/MM/YYYY'));

-- Inserindo valores iniciais na tabela "Devolucoes"
INSERT INTO Devolucoes (id_devolucao, id_emprestimo, data_devolucao)
VALUES (DEVOLUCOES_ID_DEVOLUCAO_SEQ.NEXTVAL, 1, TO_DATE('14/10/2023', 'DD/MM/YYYY'));

INSERT INTO Devolucoes (id_devolucao, id_emprestimo, data_devolucao)
VALUES (DEVOLUCOES_ID_DEVOLUCAO_SEQ.NEXTVAL, 2, TO_DATE('09/10/2023', 'DD/MM/YYYY'));
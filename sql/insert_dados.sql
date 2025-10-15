-- Inserir leitores
INSERT INTO Leitor (NOME, CPF, TELEFONE, EMAIL)
VALUES
('João Silva', '123.456.789-00', '27999999999', 'joao@email.com'),
('Maria Souza', '987.654.321-00', '27988888888', 'maria@email.com'),
('Carlos Andrade', '111.222.333-44', '27977777777', 'carlos@email.com');

-- Inserir livros
INSERT INTO Livro (TITULO, AUTOR, EDITORA, CATEGORIA, QUANTIDADE)
VALUES
('Dom Casmurro', 'Machado de Assis', 'Record', 'Romance', 3),
('O Cortiço', 'Aluísio Azevedo', 'Saraiva', 'Realismo', 4),
('Capitães da Areia', 'Jorge Amado', 'Companhia das Letras', 5);

-- Inserir empréstimos
INSERT INTO Emprestimo (ID_LEITOR, ID_LIVRO, DATA_EMPRESTIMO, DATA_DEVOLUCAO, DATA_DEV_REALIZAFA)
VALUES
(1, 2, '2025-10-15', '2025-10-25', '2025-10-15'),
(2, 3, '2025-10-14', '2025-10-24', '2025-10-14');

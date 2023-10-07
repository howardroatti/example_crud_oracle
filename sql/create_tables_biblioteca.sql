-- ============= DROP =============
-- Apaga as sequences
DROP SEQUENCE LIVROS_ID_LIVRO_SEQ;
DROP SEQUENCE USUARIOS_ID_USUARIO_SEQ;
DROP SEQUENCE EMPRESTIMOS_ID_EMPRESTIMO_SEQ;
DROP SEQUENCE DEVOLUCOES_ID_DEVOLUCAO_SEQ;

-- Apaga as tabelas
DROP TABLE Devolucoes;
DROP TABLE Emprestimos;
DROP TABLE Livros;
DROP TABLE Usuarios;

-- ============= CREATE =============

-- Cria tabela "Livros"
CREATE TABLE Livros (
  id_livro NUMBER PRIMARY KEY,
  titulo VARCHAR2(255) NOT NULL,
  autor VARCHAR2(255) NOT NULL,
  ano_publicacao NUMBER(4) NOT NULL,
  quantidade NUMBER NOT NULL --Unidades totais deste livro
  --disponibilidade NUMBER NOT NULL --Quantidade disponível para empréstimo
);

-- Cria tabela "Usuários"
CREATE TABLE Usuarios (
  id_usuario NUMBER PRIMARY KEY,
  nome VARCHAR2(255) NOT NULL,
  email VARCHAR2(255) NOT NULL,
  telefone VARCHAR2(20)
);

-- Cria tabela "Empréstimos"
CREATE TABLE Emprestimos (
  id_emprestimo NUMBER PRIMARY KEY,
  id_livro NUMBER NOT NULL,
  id_usuario NUMBER NOT NULL,
  data_emprestimo DATE NOT NULL,
  data_devolucao_sugerida DATE NOT NULL,
  FOREIGN KEY (id_livro) REFERENCES Livros(id_livro),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Cria tabela "Devoluções"
CREATE TABLE Devolucoes (
  id_devolucao NUMBER PRIMARY KEY,
  id_emprestimo NUMBER NOT NULL,
  data_devolucao DATE NOT NULL,
  --multa NUMBER(10, 2), --Nulo ou zero caso não haja multa
  FOREIGN KEY (id_emprestimo) REFERENCES Emprestimos(id_emprestimo)
);

-- Cria as sequences
CREATE SEQUENCE LIVROS_ID_LIVRO_SEQ;
CREATE SEQUENCE USUARIOS_ID_USUARIO_SEQ;
CREATE SEQUENCE EMPRESTIMOS_ID_EMPRESTIMO_SEQ;
CREATE SEQUENCE DEVOLUCOES_ID_DEVOLUCAO_SEQ;
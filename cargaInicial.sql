-- Carga inicial de dados para a tabela usuarios
INSERT INTO usuarios (nome, email) VALUES
  ('Usuário 1', 'usuario1@example.com'),
  ('Usuário 2', 'usuario2@example.com'),
  ('Usuário 3', 'usuario3@example.com'),
  ('Usuário 4', 'usuario4@example.com');

-- Carga inicial de dados para a tabela produtos
INSERT INTO produtos (nome, descricao) VALUES
  ('Produto 1', 'Descrição do Produto 1'),
  ('Produto 2', 'Descrição do Produto 2'),
  ('Produto 3', 'Descrição do Produto 3'),
  ('Produto 4', 'Descrição do Produto 4'),
  ('Produto 5', 'Descrição do Produto 5'),
  ('Produto 6', 'Descrição do Produto 6'),
  ('Produto 7', 'Descrição do Produto 7'),
  ('Produto 8', 'Descrição do Produto 8');

-- Carga inicial de dados para a tabela lista_desejos (3 produtos aleatórios para cada usuário)
INSERT INTO lista_desejos (usuario_id, produto_id, quantidade) VALUES
  (1, 1, 2), (1, 3, 1), (1, 5, 3),
  (2, 2, 1), (2, 4, 2), (2, 6, 2),
  (3, 1, 2), (3, 2, 3), (3, 7, 1),
  (4, 3, 1), (4, 5, 2), (4, 8, 3);

CREATE DATABASE gerenciador_tarefas;

USE gerenciador_tarefas;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    concluida BOOLEAN DEFAULT FALSE
);

SELECT * FROM tarefas;
'''
Exercício:
1. Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas.
As tabelas devem compreender as seguintes funcionalidades:

a. As tarefas devem ser divididas em “categorias”;
b. Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
c. As restrições/relacionamentos devem fazer sentido.

2. Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:
a. Eventos devem ter título, data e local, além da referência ao organizador;
b. O organizador deve ter nome, email e cpf;
c. As restrições/relacionamentos devem fazer sentido.

'''

import sqlite3
conexao = sqlite3.connect('./atividade/db.sqlite3')

cursor = conexao.cursor()

categoria = '''
create table categoria (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20)
),

'''
tarefa = '''
create table tarefa (
    nome VARCHAR(20),
    data VARCHAR(20),
    categoria_id INT NOT NULL,
    status_de_conclusao VARCHAR(20),
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
)

'''

cursor.execute(categoria)
cursor.execute(tarefa)
conexao.commit() 
conexao.close()

'''
CREATE TABLE categoria (
    id INT NOT NULL,
    nome VARCHAR(100),
        PRIMARY KEY (id)
);
'''
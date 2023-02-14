import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

sql_cliente = '''
CREATE TABLE cliente (
    id INTENGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100).
    cpf TEXT(14) NOT NULL,
    CONSTRAINT cliente_UN UNIQUE (cpf)
);
'''

cursor = conexao.cursor()
cursor.execute(sql_cliente)

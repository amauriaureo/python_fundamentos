import sqlite3

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()

descricao = input("Digite a descrição da categoria: ")

sql = 'insert into categoria (descricao) values (?)'

valores = [descricao]

cursor.execute(sql, valores)
conexao.commit()
conexao.close()

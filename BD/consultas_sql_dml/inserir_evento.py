import sqlite3

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()

descricao = input("Qual a descrição do evento: ")
data = input("Qual é a data do evento: ")

sql = 'select id, descricao from categoria'
categorias = cursor.execute(sql)

print("Opções de categoria:")
for categoria in categorias:
    print("ID:", categoria[0], "Descrição:", categoria[1])

categoria_id = input("Digite a categoria desejada: ")

sql = 'insert into evento (descricao, data, categoria_id) values (?, ?, ?)'

valores = [descricao, data, categoria_id]

cursor.execute(sql, valores)
conexao.commit()
conexao.close()

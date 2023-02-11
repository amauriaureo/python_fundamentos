import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

sql = 'select id, descricao, data from evento'

eventos = cursor.execute(sql)

for evento in eventos:
    print("ID: ", evento[0], "Descrição: ", evento[1], "Data: ", evento[2])

evento_id = input("Digite o ID do evento desejado: ")
nome = input("Digite o seu nome: ")
email = input("Digite o seu e-mail: ")

sql = 'insert into inscricao (evento_id, nome, email) values (?, ?, ?)'

valores = [evento_id, nome, email]

cursor.execute(sql, valores)

conexao.commit()
conexao.close()

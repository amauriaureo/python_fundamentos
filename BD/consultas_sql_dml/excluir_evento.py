import sqlite3

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()

sql = 'select id, descricao, categoria_id, data from evento'

eventos = cursor.execute(sql)
print("Eventos disponíveis: ")
for evento in eventos:
    print("ID:", evento[0], 'Descrição:', evento[1], 'Categoria:', evento[2], 'Data:', evento[3])

evento_id = input("Digite o ID do evento que você deseja apagar: ")

sql = 'delete from evento where id = ?'

valores = [evento_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()

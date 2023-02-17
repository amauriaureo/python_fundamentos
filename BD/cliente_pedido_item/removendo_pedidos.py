import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
pedido_id = input("Qual o ID do pedido que deseja remover? ")
valores = [pedido_id]
sql = 'delete from pedido where id = ?'
cursor.execute(sql, valores)
conexao.commit()
conexao.close()

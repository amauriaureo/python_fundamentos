import sqlite3
import datetime
conexao = sqlite3.connect('banco.sqlite3')
print("Insira os dados do Pedido")
cliente_id = input("Qual o ID do cliente? ")
hoje = datetime.date.today()
valores = [cliente_id, hoje]
sql_pedido = 'insert into pedido (cliente_id, data) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_pedido, valores)
print('ID do pedido:', cursor.lastrowid)

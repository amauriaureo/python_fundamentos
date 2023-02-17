import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()

# 1 — Quais as datas dos pedidos do cliente com nome Amauri?
sql_data = "select p.data from pedido as p, cliente as c where p.cliente_id = c.id and c.nome = 'Amauri'"
consulta = cursor.execute(sql_data)
for resultado in consulta:
    print(resultado)

# 2 — Quantos clientes tem a letra "A" no início do nome?
sql_letra_a = "select * from cliente where nome like 'A%'"
consulta = cursor.execute(sql_letra_a)
for resultado in consulta:
    print(resultado)

# 3 — Qual a quantidade de produtos de um determinado pedido?
pedido_id = input("Qual o ID do pedido? ")
sql_quantidade_produtos_por_pedido = 'select sum(quantidade) from item_pedido where pedido_id = ?'
consulta = cursor.execute(sql_quantidade_produtos_por_pedido, [pedido_id])
for resultado in consulta:
    print(resultado)

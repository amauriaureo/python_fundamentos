import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
print("Insira os dados dos cliente: ")
nome = input("Qual o nome do cliente? ")
cpf = input("Qual o CPF do cliente? ")
valores = [nome, cpf]
sql_inserir = 'insert into cliente (nome, cpf) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()

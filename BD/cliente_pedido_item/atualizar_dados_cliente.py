import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
cliente_id = input("Qual o ID do cliente que deseja atualizar? ")
# print("O que você deseja atualizar? \n 1. Nome; \n 2. CPF; \n 3. Todos;")
# escolha_de_alteracao = input("Escolha 1, 2 ou 3: ")
# if escolha_de_alteracao == 1:
#     nome = input("Informe o novo nome do cliente: ")
# elif escolha_de_alteracao == 2:
#     cpf = input("Informe o novo CPF do cliente: ")
# elif escolha_de_alteracao == 3:
#     nome = input("Informe o novo nome do cliente: ")
#     cpf = input("Informe o novo CPF do cliente: ")
# else:
#     print("Por favor, escolha 1, 2 ou 3.")
nome = input("Informe o novo nome do cliente: ")
cpf = input("Informe o novo CPF do cliente: ")
sql = 'update cliente set nome = ?, cpf = ? where id = ?'
valores = [nome, cpf, cliente_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()

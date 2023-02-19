import sqlite3

conexao = sqlite3.connect('rede_social.sqlite3')
cursor = conexao.cursor()

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

while True:
    senha = input("Digite sua senha: ")
    confirmar_senha = input("Confirme sua senha: ")
    if senha == confirmar_senha:
        break
    else:
        print("A confirmação de senha está errada.")

sql = 'insert into usuario(nome, email, senha) values (?, ?, ?)'

import sqlite3
import hashlib

conexao = sqlite3.connect('rede_social.sqlite3')
cursor = conexao.cursor()

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

sql = 'select count(1) from usuario where email = ? and senha = ?'

senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

valores = [email, senha]
consulta = cursor.execute(sql, valores)

existe = 0
for resultado in consulta:
    existe = resultado[0]

if existe > 0:
    print("Usuário existe!")
else:
    print("Usuário não existe!")

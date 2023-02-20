import sqlite3
import datetime

from autenticar import validar_login

conexao = sqlite3.connect('rede_social.sqlite3')
cursor = conexao.cursor()
try:
    usuario = validar_login(cursor)
except Exception as ex:
    print(ex)
    exit()

mensagem = input("Digite sua mensagem: ")
hoje = datetime.date.today()
hoje = hoje.strftime('%Y-%m-%d')

sql = 'insert into mensagem (usuario_id, mensagem, data) values (?, ?, ?)'

valores = [usuario[0], mensagem, hoje]

cursor.execute(sql, valores)
conexao.commit()
conexao.close()

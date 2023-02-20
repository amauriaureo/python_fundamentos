import sqlite3

from autenticar import validar_login

conexao = sqlite3.connect('rede_social.sqlite3')
cursor = conexao.cursor()

try:
    usuario = validar_login(cursor)
except Exception as ex:
    print(ex)
    exit()

sql = '''
select u.nome, m.texto, m.data from mensagem m inner join usuario u on m.usuario_id = u.id
where m.usuario_id in (select c.alvo_id from conexao c where c.usuario_id = ?) or m.usuario_id = ?
'''

valores = [usuario[0], usuario[0]]
consulta = cursor.execute(sql, valores)
for resultado in consulta:
    print('Nome:', resultado[0], 'Texto:', resultado[1], 'Data:', usuario[2])

conexao.close()

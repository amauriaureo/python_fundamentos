import sqlite3
conexao = sqlite3.connect('./atividades/aplicacao_de_eventos/db.sqlite3')

cursor = conexao.cursor()

sql = '''
    create table organizador (
        nome varchar (30),
        email varchar (30),
        cpf varchar not null primary key (30)
    )
'''


cursor.execute(sql)
conexao.commit()
conexao.close()

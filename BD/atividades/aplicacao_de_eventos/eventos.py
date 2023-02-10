import sqlite3
conexao = sqlite3.connect('./atividades/aplicacao_de_eventos/db.sqlite3')

cursor = conexao.cursor()

sql = '''
    create table eventos (
        titulo varchar(30),
        dia varchar(30),
        localizacao varchar(30),
        organizador_cpf varchar not null,
            FOREIGN KEY (organizador_cpf) REFERENCES organizador(cpf)
    )
'''

cursor.execute(sql)
conexao.commit()
conexao.close()

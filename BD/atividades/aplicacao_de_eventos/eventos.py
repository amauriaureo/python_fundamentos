import sqlite3
conexao = sqlite3.connect('./atividades/aplicacao_de_eventos/db.sqlite3')

cursor = conexao.cursor()

sql = '''
    create table eventos (
        titulo varchar(30),
        data varchar(30),
        local varchar(30),
        organizador_cpf int not null,
            FOREIGN KEY (organizador_cpf) REFERENCES organizador(cpf)
    )
'''

cursor.execute(sql)
conexao.commit()
conexao.close()

import sqlite3
conexao = sqlite3.connect('./atividades/gerenciador_de_tarefas/db.sqlite3')

cursor = conexao.cursor()


sql = '''
create table tarefa (
    nome VARCHAR(20),
    dia VARCHAR(20),
    categoria_id INT NOT NULL,
    status_de_conclusao VARCHAR(20),
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
)

'''

cursor.execute(sql)
conexao.commit()
conexao.close()

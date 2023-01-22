import sqlite3
conexao = sqlite3.connect('db.sqlite3')
"""
Após criar a variável “conexao”, nós precisamos criar um cursor para executar comandos SQL, tanto os DML como os DDL. 
Com a variável “cursor” criada, podemos chamar a função “execute” passando o comando SQL como parâmetro para criar nossa tabela.
"""
cursor = conexao.cursor()
cursor.execute('CREATE TABLE fornecedor(id INT, nome VARCHAR(100), endereco VARCHAR(250));')

"""
A função “commit”, associada à variável “conexao”, chamada logo em seguida, 
serve para efetivamente salvar as alterações realizadas no banco de dados.
Em seguida, a função “close” é chamada para fechar a conexão. 
Fechar a conexão é importante caso tenha algo a mais para ser executado no seu programa Python. 
Caso o programa termine após a chamada da função “commit”, a conexão será fechada de qualquer forma.
"""

conexao.commit() 
conexao.close()
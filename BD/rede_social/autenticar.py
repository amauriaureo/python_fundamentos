import hashlib


def validar_login(cursor):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    sql = 'select id, nome, email, senha from usuario where email = ? and senha = ?'

    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    valores = [email, senha]
    consulta = cursor.execute(sql, valores)

    usuario = None
    for resultado in consulta:
        usuario = resultado
        break

    return usuario

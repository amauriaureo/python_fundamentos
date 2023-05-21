"""
Debugando com PDB

PDB -> Python Debugger

# OBS: A utilização d print() para debugar código e uma prática ruim.


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

"""
# Existem formas mais profissionais de se fazer esse 'debug',
# utilizando o debugger em Python, podemos fazer isso em diferentes IDE's,
# como o PyCharm ou utilizando o PDB - Python Debugger.

# Exemplo com o PDB - Python Debugger

# Para utilizar  Python Debugger, precisamos importar a biblioteca pdb
# e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


import pdb

nome = 'Amauri'
sobrenome = 'Rodrigues'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

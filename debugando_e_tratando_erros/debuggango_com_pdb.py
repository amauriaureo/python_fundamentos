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
# import pdb; pdb.set_trace() ****
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)


# **** Porque utilizar o debugger nesse formato?
# import pdb; pdb.set_trace() ****
# O debug é utilizado durante o desenvolvimento.
# Costumamos realizar todos os imports de bibliotecas no início do arquivo.
# Por isso, ao invés de colocarmos o import do pdb no início do arquivo,
# nós colocamos somente onde vamos debuggar,
# e ao finalizar já fazemos a remoção.
"""

# A partir do Python 3.7, não é
# mais necessário importar a biblioteca pdb, pois o comando de debug
# foi incorporado como função bulti-in (integrada) chamada breakpoint()


nome = 'Amauri'
sobrenome = 'Rodrigues'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

"""
Trabalhando com Modulos Builtin (módulos integrados,
que já vem instalados eno Python)


"""

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Amauri', 'Rodrigues', 'Python']
shuffle(lista)
print(lista)

print(choice('Rodrigues'))

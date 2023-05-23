"""
Trabalhando com Modulos Builtin (módulos integrados,
que já vem instalados eno Python)

https://docs.python.org/3/py-modindex.html

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

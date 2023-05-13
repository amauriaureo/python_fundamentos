"""
Reversed

OBS: Não confundir com reserver() - listas

lista = [1, 2, 3, 4, 5]
print(lista)
lista.reverse()
print(lista)

A função reverse() só funciona e [listas].

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado 'list_reverseiterator'
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto.

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
print(set(reversed(lista)))

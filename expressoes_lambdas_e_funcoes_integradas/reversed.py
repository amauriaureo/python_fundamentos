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
print(set(reversed(lista)))  # No set não definimos ordem.

# Podemos iterar sobre o reversed
for letra in reversed('Amauri Rodrigues'):
    print(letra, end='')

print('\n')
# Iterando sem o uso do for
print(''.join(list(reversed('Amauri Rodrigues'))))

# Slice de Strings

print('Amauri Rodrigues'[::-1])

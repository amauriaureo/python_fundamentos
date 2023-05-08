"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quiseremos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxy

{chave: valor for valor in iteravel}  # Dict Compr
[valor for valor in iteravel]  # List Compr
"""

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(numeros.items())
print(quadrado)


numeros_lista = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros_lista}

print(quadrados)

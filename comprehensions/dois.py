"""
List Comprehension

Podemos adicionar estruturas condicionais lógicas.
"""

# Exemplos.

# 1.
numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

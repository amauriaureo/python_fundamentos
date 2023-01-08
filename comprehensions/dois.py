"""
List Comprehension

Podemos adicionar estruturas condicionais lógicas.
"""

# Exemplos.

# 1.
numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

#Refatorar

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]


print(pares)
print(impares)

# 2.

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

Set não guarda ordenação, não aceita valores repetidos.

"""

# Exemplos

# 1.
numeros = {num for num in range(1, 7)}
print(numeros)

# 2.
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio! Fazer alteração na estrutura acima para gerar um dicionário
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# 3.
letras = {letra for letra in 'Python e Django'}
print(letras)

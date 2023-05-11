"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort().

O sort() só funciona com listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar,

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados


# Exemplo

numeros = (6, 1, 8, 10)  # () [] ou {}
print(numeros)
print("set:", set(sorted(numeros)))  # Ordena do menor para o maior
print("tuple:", tuple(sorted(numeros)))
print("lista:", list(sorted(numeros)))
print(numeros)

print(sorted(numeros, reverse=True))
"""

# Utilizando sorted() para coisas mais complexas.

usuarios = [
    {"username": "samuel", "tweets": ["Um", "Dois"]},
    {"username": "joana", "tweets": ["Um"]},
    {"username": "dylanmaster", "tweets": [], "cor": "amarelo"},
    {"username": "crazylapton", "tweets": ["1", "2", "3"]},
    {"username": "jandira123", "tweets": ["1", "2", "3", "4"], "cor": "preto", "musica": "rock"},
]

print(usuarios)

print(sorted(usuarios, key=len))

# Ordenando pelo username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

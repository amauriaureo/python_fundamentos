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
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "joana", "tweets": ["Eu adoro meu cachorro"]},
    {"username": "dylanmaster", "tweets": [], "cor": "amarelo"},
    {"username": "crazylapton", "tweets": ["Fui passear com meu cachorro"]},
    {"username": "jandira123", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)

print(sorted(usuarios, key=len))

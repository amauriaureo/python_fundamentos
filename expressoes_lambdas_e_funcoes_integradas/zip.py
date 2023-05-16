"""
zip1

zip() -> Cria um iterável(Zip object) que agrega elemento
de cada um dos iteraveis passados como entrada em pares.
"""

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip)
print(type(zip))

# Gerando Lista, Tupla ou Dicionário,

print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# O zip utiliza como parâmtro o menor tamanho em iterável.
# Então, se estiver trabalhando com iteráveis de tamanho diferentes,
# irá parar quando os elementos do menor iterável acabar.

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

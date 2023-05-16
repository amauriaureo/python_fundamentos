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

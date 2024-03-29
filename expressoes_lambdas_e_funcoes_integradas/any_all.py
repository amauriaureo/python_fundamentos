"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.


# Exemplo all()

# False
print(all([0, 1, 2, 3, 4]))

# True
print(all([1, 2, 3, 4]))
print(all({1, 2, 3, 4}))
print(all((1, 2, 3, 4)))
print(all([]))
print(all(['Olá, mundo!']))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# print(all())

print(all([letra for letra in 'eio' if letra in 'fkp']))  # retorna '[]' vazio True
print(bool([]))  # False

print(all([num for num in [4, 2, 10, 8, 4] if num % 2 == 0]))


any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
"""
print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), []]))  # False
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(all([nome[0] == 'C' for nome in nomes]))  # False

print(any([num for num in [4, 2, 10, 6, 9, 8] if num % 2 == 0]))  # True

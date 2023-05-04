"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

"""

# Exemplo all()

print(all([1, 2, 3, 4]))  # True
print(all({1, 2, 3, 4}))  # True
print(all((1, 2, 3, 4)))  # True
print(all([]))  # True

print(all([0, 1, 2, 3, 4]))  # False

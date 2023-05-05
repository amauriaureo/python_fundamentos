


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))


# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator - Ocupa menos espaço na memória.
rez = (nome[0] == 'C' for nome in nomes)
print(type(rez))
print(rez)

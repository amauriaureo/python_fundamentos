import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map

# Map e uma função que receber dois parâmetros: O primeiro a função, o segundo um iteravel. Retorna um Map Object

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com Labda.

print(list(map(lambda r: math.pi * (r ** 2), raios)))

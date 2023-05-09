"""
Generators

Em aulas anteriores(Comprehension), estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... porque eas se chamem Generators


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

"""
# Qual é a utilidade de getsizeof()? ->
# getsizeof - pega o tamanho de.
# Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof

print(getsizeof('Geek'))

print(getsizeof('University'))

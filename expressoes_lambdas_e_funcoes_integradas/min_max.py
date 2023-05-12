"""
Min e Max

max() retorna o maior valor em um iterável ou o maior de dois ou mais elementos

"""

# Exemplos

lista = [1, 8, 10, 100, 327]
print(max(lista))

tupla = (1, 8, 10, 100, 327)
print(max(tupla))


conjunto = {1, 8, 10, 100, 327}
print(max(conjunto))

dicionario = {"a": 1, "b": 8, "c": 10, "d": 100, "e": 327}
print(max(dicionario))
print(max(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior
# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))
# print(max(val1, val2))

print(max(6, 67, 90))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'd'))
print(max(3.145, 5.789))
print(max("Amauri Rodrigues"))

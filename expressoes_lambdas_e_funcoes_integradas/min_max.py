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

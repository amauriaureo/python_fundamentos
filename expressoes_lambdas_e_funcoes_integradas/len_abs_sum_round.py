"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o número de itens(tamanho) do iterável
"""
# Exemplos

print(len([1, 2, 3, 4]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5, 6}))
print(len('Amauri '))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
print(len(range(0, 9)))
# Por baixo dos panos está sendo executado o Dunder len()
print('Amauri Rodrigues'.__len__())

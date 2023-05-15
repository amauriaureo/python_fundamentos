"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o número de itens(tamanho) do iterável
# Exemplos

print(len([1, 2, 3, 4]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5, 6}))
print(len('Amauri '))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
print(len(range(0, 9)))
# Por baixo dos panos está sendo executado o Dunder len()
print('Amauri Rodrigues'.__len__())


# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real,
De forma basica seria o seu valor real sem o sinal.

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# Sum

sum() -> Recebe como parâmetro um iteravel, podedo receber um valor inicial,
e retorna a soma total dos elementos, incluindo o valor inicial.

OBS: O valor iniciail default = 0
"""
print(sum([1, 2, 3, 4, 5], -5))

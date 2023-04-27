"""
Reduce

OBS: A partir do Python3+ a função reduce()
não e mais uma função integrada (built-in).
Agora temos que utilizar esta função a partir do módulo 'funtools'

Guido von Rossum: Utilize a função reduce() se você realmente precisa dela,
Em todo caso, 99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
"""

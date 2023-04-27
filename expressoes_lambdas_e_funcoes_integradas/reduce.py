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

Assim como map() e filter(), a função reduce() recebe dois parâmetros:
1. a função e 2. o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2)
# Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3)
# Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o resultado.
E isso é repetido até o final.
"""

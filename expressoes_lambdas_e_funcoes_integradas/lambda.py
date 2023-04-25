"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simpesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.


"""

# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

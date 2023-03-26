"""
Funções de Maior Grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programação suporte HOF,
indica que podemos ter funções que retornam outras funções
como resultado ou mesmo que podemos passar funções como
argumentos para outras funçõesm e até mesmo
criar variáveis do tipo de funções nos nossos programas.

Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizen.

"""


def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 2, somar))
print(calcular(4, 2, multiplicar))
print(calcular(4, 2, dividir))
print(calcular(4, 2, subtrair))

"""
Nested Functions - Funções aninhadas

Em Python podemos tambem ter funções dentro de funções,
que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas).
"""

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('Oi, ', 'Ola, ', 'Hello, '))
    return humor() + pessoa


print(cumprimento('Ana'))
print(cumprimento('Maria'))

"""
Retornando funções de outras funções
"""


def faz_me_rir():
    def rir():
        return choice(("hahaha", "kkkkkkk", "rsrsrsrs"))
    # return rir
    return rir()


# rindo = faz_me_rir()
# print(rindo())
print(faz_me_rir())
"""
Inner Functions ( Funções Internas / Nested Functions)
podem acessar o escopo de funções mais externa

Exemplos acima: funções humor pode acessar o escopo
de cumprimento e até mesmo o argumento "pessoa"
"""


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'kkkkkk', 'rsrsrsrs'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())

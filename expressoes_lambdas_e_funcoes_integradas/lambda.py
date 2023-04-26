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

# Expressões lambdas com multiplas entradas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo("  bOb  ", "dYLAN   "))
print(nome_completo("  kEITH  ", "     RICHARDs   "))

# Em funções Python, podemos ter nenhuma ou varias entradas. Em Lambdas também.

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo

influencers = ['Isaac Asimov', 'Ray Charles', 'Travis Barker',
               'Taylor Hawkins', 'Jim Carey', 'Will Smith',
               "Henry David Throreau", "Paulo Coelho" ]

print(influencers)

influencers.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(influencers)


# FUnção Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
print(teste(3))

print(geradora_funcao_quadratica(2, 3, -5)(2))

# Expressoes Lambdas são utilizadas para ordenar e filtrar dados,
# mas não se limitam a isso

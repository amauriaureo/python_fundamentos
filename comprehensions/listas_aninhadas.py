"""
Listas Aninhadas (Nested Lists)
Em outras linguagens: Arrays ou vetores multidimensionais
Em Python: Listas Aninhadas

- Algumas linguagens de programação (C/Java/PHP)
possuem uma estrutura de dados chamadas de arrays:

    * Unidimensionais (Arrays/Vetores);
    * Multidimensionais (Matrizes);


Em Python nós temos as Listas

numeros = [1, 'b', 2.65, True, 4, 5]
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix 3X3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0])  # [1, 2, 3]
print(listas[0][1])  # 2
print(listas[2][1])  # 8
print(listas[2][-2])  # 8

# Iterando com loops em uma lista aninhada
print('*' * 100)

for lista in listas:
    print(lista)

print('*' * 100)

for lista in listas:
    for num in lista:
        print(num)

print('List Comprehension: ')

[[print(valor) for valor in lista] for lista in listas]

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range (1, 4)]
print(tabuleiro)

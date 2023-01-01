"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

"""

# Exemplos 

numeros = [1, 2, 3, 4, 5]
# Loop 

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehension
res = [numero * 2 for numero in numeros]
print(res)

# 1
nome = "Amauri Rodrigues"

print([letra.upper() for letra in nome])

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['julia', 'luana', 'joão', 'caique']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero * 3 for numero in range (1, 10)])


# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])


# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])


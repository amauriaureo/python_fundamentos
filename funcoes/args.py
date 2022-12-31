def somar_numeros(nome, *args):
    return sum(args)

numero = [1, 2, 3, 44, 5]

# Desempacotador:
print(somar_numeros(*numero))
print(somar_numeros('SP', 1, 2, 3, 42))


def somatorio(*args):
  soma = 0
  for numero in args:
    soma += numero
  return soma
print(somatorio(10,9,5,6,3,4))


def verificar_info(*args):
    if 'Amauri' in args and 'Junior' in args:
        return('Amauri Junior! Seja bem vindo!')
    return('Desculpe. Seu nome não consta no banco de dados.')

print(verificar_info('Amauri', 'Junior', 'Campinas', 'São Paulo'))
print(verificar_info('Amauri', 'Campinas', 'São Paulo'))
print(verificar_info('Junior', 'Campinas', 'São Paulo'))
print(verificar_info(1, 42, 'Campinas', 'São Paulo'))


def unir_palavras(*args):
    return '_'.join(args)

print(unir_palavras('a','b', 'c'))
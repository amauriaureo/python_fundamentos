"""
Try / Except / Else / Finally

Dica de quando e onde tratar código.

TODA ENTRADA DEVE SER TRATADA.

# Else -> Executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um numero:'))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')


# Finally

try:
    num = int(input('Informe um número'))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não
# O finally geralmente é utilizado para fechar ou desalocar recursos.


# Exemplo mais complexo !!!ERRADO!!!


def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
"""
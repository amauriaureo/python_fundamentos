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

# Exemplo mais complexo !!!CORRETO!!!
# Responsabilidade pelas entradas das suas funções.


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError as erra:
        return f'Valor incorreto. Erro: {erra}'
    except ZeroDivisionError as errb:
        return f'Não e possível realizar uma divisão por zero. Erro: {errb}'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
print(dividir(num1, num2))
"""

# Exemplo mais complexo semi-generico.


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'ocorreu um problema'


num1 = input('Informe o primeiro número')
num2 = input('Informe o segundo número')

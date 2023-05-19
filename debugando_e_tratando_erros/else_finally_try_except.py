"""
Try / Except / Else / Finally

Dica de quando e onde tratar código.

TODA ENTRADA DEVE SER TRATADA.

"""

try:
    num = int(input('Informe um numero:'))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')

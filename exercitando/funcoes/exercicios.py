'''
1.
def dobro_do_valor(numero):
    print(numero * 2)

dobro_do_valor(2)

2.

dia = int(input('Digite o dia:'))    
mes = int(input('Digite o mês:'))
ano = int(input('Digite o ano:'))

if mes == 1:
    mes = 'janeiro'
elif mes == 2:
    mes = 'fevereiro'
elif mes == 3:
    mes = 'março'
elif mes == 4:
    mes =  'abril'
elif mes == 5:
    mes = 'maio'
elif mes == 6:
    mes = 'junho'
elif mes == 7:
    mes = 'julho'
elif mes == 8:
    mes = 'agosto'
elif mes == 9:
    mes = 'setembro'
elif mes == 10:
    mes = 'outubro'
elif mes == 11:
    mes = 'novembro'
elif mes == 12:
    mes = 'dezembro'
else:
    print('número inválido')

if dia < 10:
    print(f'0{dia} de {mes} de {ano}.')
else:
    print(f'{dia} de {mes} de {ano}.')

3.

def negativo_positivo(numero):
    if numero > 0:
        print(1)
    elif numero < 0:
        print (-1)
    else:
        print(0)

negativo_positivo(0)
negativo_positivo(10)
negativo_positivo(-9)

4
'''
import math

def quadrado_perfeito(numero):
    raiz_quadrada = math.sqrt(numero)
    print(raiz_quadrada - math.floor(raiz_quadrada) == 0) 

numero = int(input('Informe um valor inteiro:'))

# number = quadrado_perfeito(numero)

if numero == True:
    print(f'O número {numero} é um quadrado perfeito.')
else:
    print(f'O {numero} não é um quadrado perfeito.')



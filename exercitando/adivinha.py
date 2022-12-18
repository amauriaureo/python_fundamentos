from random import randint
numero = randint(1, 50)
tentativa = 0
while tentativa < 5:
    sorte = int(input('Digite um numero:'))
    if sorte == numero:
        print('Você acertou!')
    elif sorte < numero:
        print(f'O número que você digitou é menor do que o sorteado.')
    elif sorte > numero:
        print(f'O número que você digitou é maior do que o sorteado.')
    else:
        print('Inválido.')
    tentativa +=1
print(f'fim do programa. O número era {numero}')
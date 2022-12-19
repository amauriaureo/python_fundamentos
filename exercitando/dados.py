from random import randint

escolha = int(input("Insira o número de tentativa: "))
tentativa = 1
valores = []

while tentativa <= escolha:
    dados = randint(1, 6)
    print(dados)
    valores.append(dados)

    tentativa += 1


print(valores)
print("Total: ", sum(valores))
print("Média: ",sum(valores) / escolha)
print("Maior: ", max(valores))
print("Menor: ", min(valores))
print("FIM DO PROGRAMA!")
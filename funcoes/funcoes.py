def apresentacao(nome, idade):
    print(f'Olá, {nome}! Sua idade é {idade}.')

# from funcoes import apresentacao
# apresentacao('Nome de alguém', 300)

def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

# from funcoes import juros_simples
# juros_simples(1000, 2, 12)

# 1. Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar (utilizando **kwargs).

def par_impar(**kwargs):
    numero = kwargs.get('numero')
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

par_impar(numero=6)

# 2. Crie de forma recursiva uma função que printe do número recebido até o zero.
# A)
def funcao_recebida(numero):
    print(numero)
    while numero > 0:
        funcao_recebida(numero - 1)
        break
    
funcao_recebida(numero=10)

# B)

def contagem_decrescente(numero):
  print(numero)
  if numero > 0:
    contagem_decrescente(numero-1)

numero = int(input())
contagem_decrescente(numero)

# 3. Crie uma função de somatório que some todos os números que a função receber (usando *args).
# A)
def somar_numeros(*args):
    return sum(args)
    
numero = [30, 7]
print(somar_numeros(*numero))

# B)
def somatorio(*args):
  soma = 0
  for numero in args:
    soma += numero
  return soma
print(somatorio(10,9,5,6,3,4))


# 4. Crie um programa com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
# A)
def tres_argumentos(a, b, c):
    print(a + b + c)
    
tres_argumentos(2, 3, 4)

# B)
def soma_argumentos(numero, numerob, numeroc):
    return numero + numerob + numeroc

print(soma_argumentos(1,5,3))

# 5. Faça um programa com uma função que necessite de um argumento. A função deve retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
# A)

def programa_argu(argumento):
    if argumento > 0:
        print('P')
    print('N')
    
programa_argu(-10)

# B)
def verifica_numero(numero):
    if numero > 0:
       return 'P'
    else:
       return 'N'

numero = int(input())
print(verifica_numero(numero))

# 6. Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
# A)
frase = 'Uma Frase Qualquer'.upper()
contador = frase.count('A')
print(format(contador))

# B)
def contagem_letra(palavra, letra_procurada):
   contador = 0
   for letra in palavra:
      if letra == letra_procurada:
         contador += 1
   return contador

print(contagem_letra("paralelepipedo", "p"))

# 7. Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.
# A)

def gorjeta(valor):
    return valor*0.1
    
print(gorjeta(1000))

# B)
def calcula_gorjeta(valor_conta):
   return valor_conta * 0.1

numero = int(input())
print(calcula_gorjeta(numero))

# 8. Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda.
# Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.
# A)
def checar(prefixo, palavra):
    tamanho = len(prefixo)
    return prefixo ==palavra[:tamanho]

print(checar('uf', 'ufab'))
print(checar('ufab', 'uf'))

# B)
def verifica_prefixo(prefixo, palavra):
   
   if palavra[:len(prefixo)] == prefixo:
      return True
   
   else:
      return False

print(verifica_prefixo("para","paralelepipedo"))
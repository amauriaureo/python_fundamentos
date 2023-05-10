"""
Generators

Em aulas anteriores(Comprehension), estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... porque eas se chamem Generators


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))


# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator - Ocupa menos espaço na memória.
rez = (nome[0] == 'C' for nome in nomes)
print(type(rez))
print(rez)

"""
# Qual é a utilidade de getsizeof()? ->
# getsizeof - pega o tamanho de.
# Retorna a quantidade de bytes em memória do elemento passado como parâmetro.

from sys import getsizeof

"""
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(99))

print(getsizeof(6858626379263792697362963232))

print(getsizeof(True))
"""
# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))


print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')


"""
Generator ocupou 104 bytes(+ leve).
Ele ocupa tão pouco byte pois ele não gerou nada ainda,
apenas deixou tudo preparado para quando precisar utilizar e,
quando utilizar, ele gera em memória e apaga em memória, ele não fica ocupando,
já os Comprehensions ficarão em memória até o final do programa.
"""

# Iterando com Generator Expression

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

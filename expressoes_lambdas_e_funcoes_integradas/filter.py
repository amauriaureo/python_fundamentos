"""
filter() Serve para filtrar dados de uma determinada coleção.
"""
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter()
# eles são excluidos da memória

paises = ['Cuba', '', 'Venezuela', '', 'Equador', '', 'Argentina', '', 'Brasil']
res = filter(None, paises)
res2 = filter(lambda pais: len(pais) > 0, paises)
res3 = filter(lambda pais: pais != '', paises)
print('res: ', list(res))
print('res2: ', list(res2))
print('res3: ', list(res3))

# Diferença entre map() e filter():
# map() recebe dois params, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.
# filter() recebe dois params, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

# Exemplo mais complexo.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "joana", "tweets": ["Eu adoro meu cachorro"]},
    {"username": "dylanmaster", "tweets": []},
    {"username": "crazylapton", "tweets": ["Fui passear com meu cachorro"]},
    {"username": "jandira123", "tweets": []},
]

# Filtrar os usuarios que estão inativos no Twitter.

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

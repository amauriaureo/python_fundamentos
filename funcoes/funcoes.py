def apresentacao(nome, idade):
    print(f'Olá, {nome}! Sua idade é {idade}.')

# from funcoes import apresentacao
# apresentacao('Nome de alguém', 300)

def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

# from funcoes import juros_simples
# juros_simples(1000, 2, 12)
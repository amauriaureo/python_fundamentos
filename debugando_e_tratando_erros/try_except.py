"""
O block try/except

Utilizamos o bloco try/except para tratar erros
que podem ocorrer no nosso código. Previnindo assim,
que o programa pare de funcionar e o usuário receba
mensagens de erro inesperadas.

A forma geral mais simples e:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema...')

geek()

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema...')



OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros.
O ideal é SEMPRE tratar de forma especifica.
"""
# Exemplo 3 - Tratando um erro específico.

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente...')
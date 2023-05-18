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

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros.
O ideal é SEMPRE tratar de forma especifica.
"""

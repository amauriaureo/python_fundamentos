"""
Em Python, Módulos são arquivos.

Módulo Random ->
Possui várias funções para geração de números pseudo-aleatório.

Dentro do módulo Random existe a função random

Pode importar todo o módulo com:
import random
Ou melhor, importar funções especificas.

Assim ocupa menos memória.

from random import random

for i in range(10):
    print(random())

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não e incluído.
"""
# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # de 1 a 60

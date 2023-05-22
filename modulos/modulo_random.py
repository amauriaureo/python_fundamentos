"""
Em Python, Módulos são arquivos.

Módulo Random ->
Possui várias funções para geração de números pseudo-aleatório.

Dentro do módulo Random existe a função random

Pode importar todo o módulo com:
import random
Ou melhor, importar funções especificas.

Assim ocupa menos memória.
"""

from random import random

for i in range(10):
    print(random())

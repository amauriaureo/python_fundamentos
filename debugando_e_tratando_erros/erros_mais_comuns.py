"""
Erros mais comuns.

1 - SyntaxError
Erro de sintaxe. Quando Python não reconhece como parte da lingugagem.


2 - NameError
Quando uma variavél ou função não foi definida


3 - TypeError
Quando uma função/operação/ação é aplicada a um tipo errado.
Exemplo:
A) "print(len(5))"
# TypeError: object of type 'int' has no len()

B) print("Geek" + [])
# TypeError: can only concatenate str (not "list") to str


4 - IndexError
Quando tebtamos acessar um elemento em uma lista ou
outro tipo de dado indexado utilizando um indice inválido.


5 - ValueError
Quando uma função/operação built-in (integrada) recebe
um argumento com tipo correto mas valor inapropriado
Exemplos:
print(float('String'))
#  ValueError: could not convert string to float: 'String'

print(int('String'))
#  ValueError: invalid literal for int() with base 10: 'String'


6 - KeyError
Quando tentamos acessar um dicionário com uma chave que não existe.


7 - AttributeError
Quando uma variável não tem um atributo/função.
Exemplo:
tupla = (11, 22, 33, 44)
print(tupla.sort())
#  AttributeError: 'tuple' object has no attribute 'sort'
OBS: se fosse uma [lista] não teria erro.


8 - IndentationError
Quando não respeitamos a indentação do Python(4 espaços)

"""

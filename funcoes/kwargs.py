def encontrando_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)

encontrando_funcao('Juanito', 24, 4, 3, 5, solteiro = True, python='isso!!', javascript='bora lá', cobol= False)

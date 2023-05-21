"""
Debugando com PDB

PDB -> Python Debugger

# OBS: A utilização d print() para debugar código e uma prática ruim.


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

"""

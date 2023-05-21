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
# Existem formas mais profissionais de se fazer esse 'debug',
# utilizando o debugger em Python, podemos fazer isso em diferentes IDE's,
# como o PyCharm ou utilizando o PDB - Python Debugger.

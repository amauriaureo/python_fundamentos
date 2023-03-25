def decorator_imprimir(funcao):
    def valores(capital, taxa, tempo):
        print(f"CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}")
        print(f"RESULTADO: {funcao(capital, taxa, tempo)}")
    return valores


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo


if __name__ == "__main__":
    juros_simples(1000, 5, 6)

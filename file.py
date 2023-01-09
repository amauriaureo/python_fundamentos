class CaixaEletronico:
    
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome

    def sacar(self, valor_saque):
        
        #Comece aqui seu código
    
    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))

if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(valor)
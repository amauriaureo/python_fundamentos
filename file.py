class CaixaEletronico:
    
    def __init__(self, nome):
        #              0   1   2   3   4
        self.notas = [100, 50, 20, 10, 5, 2, 1]
        self.nome_banco = nome

    def saldo(self, valor_saque):
      ########################################
        #Comece aqui seu código
        indice = 0
        restante = valor_saque

        #        V
        #Indice: 0  1  2  3  4
        #Notas: 100 50 20 10 5  2  1
        saque = [0, 0, 0, 0, 0, 0, 0]

        while restante > 0:
          nota_atual = self.notas[indice]
          
          #Saque
          if nota_atual <= restante:
            restante -= nota_atual
            saque[indice] += 1
          else:
            indice += 1
        ########################################
        print(saque)
        self.sacar(saque) #Chamando a função a partir da própria classe
    
    def sacar(self, notas):
      for indice in range( len(notas) ):
        if notas[indice] > 0:
          print(f"Retire {notas[indice]} notas de {self.notas[indice]}")

if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.saldo(valor) #Chamando a função (método) a partir do objeto
# O objetivo do exercício, é criar um programa para gerenciar uma cartela de investimentos. Para isto, deverão ser implementadas as classes do diagrama anexado a seguir.

# -> A classe Portfolio que possui uma lista de investimentos passada como entrada no construtor e um método rendimento() que deve retornar a soma dos rendimentos da lista de investimentos. Os tipos de investimentos possíveis são RendaFixa, CompraVenda (compra e venda de itens), Imóvel e Acoes.

# -> A classe abstrata Investimento tem como atributos o nome do investimento e o valor investido. Ela tem como método abstrato rendimento(). Todas as classes que herdam de Investimento devem implementar este método.

# -> A classe RendaFixa herda de Investimento e tem como atributos adicionais a duração do investimento em meses e a taxa de juros mensais. Sua implementação do método rendimento() deve retornar os juros totais após a duração do investimento.

# -> A classe CompraVenda também herda de Investimento e tem como atributo adicional o valor de venda do bem. Sua implementação do método rendimento() deve retornar a diferença entre o preço de venda e o preço de compra.

# -> A classe Acoes herda de CompraVenda e tem como atributo adicional o valor total de dividendos recebido pelas ações. Ela deve sobrescrever o método rendimento() de CompraVenda e somar ao resultado o valor dos dividendos.

# -> Por fim, a classe imóvel herda de CompraVenda e tem como atributos adicionais os gastos_mensais do imóvel quando este não está alugado, o número de meses que ele ficou alugado, o valor do aluguel e a duração do investimento em meses (quantos meses se passaram entre a compra e a venda do imóvel). Sua implementação do método rendimento() deve além de calcular a diferença entre valor de venda e compra, deve subtrair os gastos do imóvel nos meses em que ele não esteve alugado e somar os valores dos aluguéis nos demais meses.

from abc import ABC, abstractmethod

class Portfolio():
    def __init__(self, listaInvest) -> None:
        self.listaInvest = listaInvest

    def rendimento(self):
        rendTotal = 0
        for rend in self.listaInvest:
            rendTotal += rend.rendimento()
        return rendTotal

class Investimento(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        pass

    @abstractmethod
    def rendimento(self):
        pass

class RendaFixa(Investimento):
    def __init__(self, nome, valor_investido, taxa, duracao) -> None:
        super().__init__()
        self.valor_investido = valor_investido
        self.duracao = duracao
        self.taxa = taxa

    def rendimento(self):
        # jurosTotais = (self.valor_investido * self.taxa) * self.duracao
        jurosAtual = self.valor_investido
        for _ in range(self.duracao):
            jurosAtual += jurosAtual * self.taxa

        return jurosAtual - self.valor_investido
    
class CompraVenda(Investimento):
    def __init__(self, nome, valor_investido, valor_venda) -> None:
        super().__init__()

        self.valor_venda = valor_venda
        self.valor_investido = valor_investido
    
    def rendimento(self):
        dif = self.valor_venda - self.valor_investido
        return dif
    
class Acoes(CompraVenda):
    def __init__(self, nome, valor_investido, valor_venda, dividendos) -> None:
        super().__init__(nome, valor_investido, valor_venda)
        self.dividendos = dividendos

    def rendimento(self):
        rend = self.valor_venda - self.valor_investido + self.dividendos
        return rend

class Imovel(CompraVenda):
    def __init__(self, nome, valor_investido, valor_venda, gastos_mensais, meses_alugados, aluguel, duracao) -> None:
        super().__init__(nome, valor_investido, valor_venda)
        self.gastos_mensais = gastos_mensais
        self.meses_alugados = meses_alugados
        self.aluguel = aluguel
        self.duracao = duracao

    def rendimento(self):
        meses_nao_alugados = self.duracao - self.meses_alugados
        total_aluguel = self.aluguel * self.meses_alugados
        total_gastos = self.gastos_mensais * meses_nao_alugados

        dif = self.valor_venda - self.valor_investido
        rend = dif - total_gastos + total_aluguel

        return rend
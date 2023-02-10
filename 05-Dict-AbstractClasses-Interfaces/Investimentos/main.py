from investimentos import (Portfolio, RendaFixa, CompraVenda, Imovel, Acoes)


def main():
    portfolio = Portfolio([
        RendaFixa("poupanca", valor_investido=1000, taxa=0.007, duracao=48),
        RendaFixa("LCI-2025", valor_investido=5000, taxa=0.012, duracao=24),
        CompraVenda("Carro", valor_investido=32000, valor_venda=35000),
        Imovel("Casa", valor_investido=150000, valor_venda=170000,
        gastos_mensais=900, meses_alugados=12, aluguel=1600, duracao=24),
        Acoes("Americanas", valor_investido=6000, valor_venda=1000, dividendos=47),
    ])

    rendimento_total = portfolio.rendimento()
    print(f"{rendimento_total:.2f}")


if __name__ == "__main__":
    main()
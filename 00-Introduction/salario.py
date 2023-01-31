# Suponha que um trabalho pague 
# 5% do salário de seus funcionários como contribuição do INSS 
# e uma previdência privada de 2%. 
# Faça um programa que leia o salário de uma pessoa, 
# e mostre na tela os valores das contribuições 
# e o salário líquido após os descontos com 2 casas após a vírgula.

def main():
    salario = float(input())
    pctInss = 0.05
    pctPrevPriv = 0.02

    inss = pctInss * salario
    prevPriv = pctPrevPriv * salario
    salarioLiq = salario * (1 - (pctInss + pctPrevPriv))

    print(f'INSS: {inss:.2f}')
    print(f'Previdência Privada: {prevPriv:.2f}')
    print(f'Salário líquido: {salarioLiq:.2f}')

if __name__ == '__main__':
    main()
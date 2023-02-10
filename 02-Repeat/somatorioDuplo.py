# Faça um programa que leia um número inteiro n, 
# e mostre na tela o resultado da soma abaixo com 3 casas após a vírgula.

# sumi=1 até n sumj=1 até n 1 / ((i + j) ** 2)

def main():
    somaInterna = 0
    somaExterna = 0

    n = int(input()) + 1

    for i in range(1, n):
        for j in range(1, n):
            somaInterna += 1 / ((i + j) ** 2)
        somaExterna += somaInterna

    print(f'{somaInterna:.3f}')

if __name__ == "__main__":
    main()
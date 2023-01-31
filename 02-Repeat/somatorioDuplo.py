# Faça um programa que leia um número inteiro n, 
# e mostre na tela o resultado da soma abaixo com 3 casas após a vírgula.

# sumi=1 até n sumj=1 até n 1 / ((i + j) ** 2)

def main():
    soma = 0
    soma2 = 0

    n =int(input())

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            soma += i / ((i + j) ** 2)
        soma2 += soma

    print(f'{soma:.3f}, {soma2:.3f}')

if __name__ == "__main__":
    main()
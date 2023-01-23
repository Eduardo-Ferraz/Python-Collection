# Abaixo são listadas algumas sequências de números. 
# Cada número da sequência possui um índice, sendo o primeiro 0, o segundo 1 e assim por diante. 
# Faça um programa que leia o índice i de um número 
# e mostre na tela o i-ésimo elemento de cada sequência, um por linha.

# 0, 1, 2, 3, 4, 5, 6, …
# 4, 5, 6, 7, 8, 9, …
# 0, 9, 18, 27, 36, …
# 1, -1, 1, -1, 1, -1, …
# 2, 3, 5, 9, 17, 33, 65, …

import math

def main():
    n = int(input())
    numbers = []
    quarta = []

    numbers.append(n)
    numbers.append(n + 4)
    numbers.append(n * 9)
    numbers.append(pow(-1, n))

    quarta.append(2)
    for i in range(1, n + 1):
        quarta.append(2 * quarta[i-1] - 1 )

    numbers.append(quarta[n])

    for num in numbers:
        print(num)

if __name__ == '__main__':
    main()
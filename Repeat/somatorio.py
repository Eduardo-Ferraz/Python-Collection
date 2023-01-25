# Faça um programa que leia um número n >= 1 e 
# mostre na tela o resultado da soma de {1/i2} 
# para i variando de 1 a n (incluindo n) 
# com 3 casas após a vírgula.

def main():
    soma = 0
    n =int(input())

    for i in range(1, n + 1):
        soma += 1 / i ** 2

    print(f'{soma:.3f}')

if __name__ == "__main__":
    main()
# Suponha que uma bola seja lançada a partir da posição 0 em uma roleta com tamanho n. 
# Suponha ainda que você saiba que ela vai passar por k casas. 
# Faça um programa leia os valores de n e k 
# e mostre na tela o número de voltas completas que a bola irá dar na roleta 
# e em qual casa ela irá terminar.

def main():
    numbers = input().split()

    tamanho = int(numbers[0])
    casasParaPassar = int(numbers[1])
    voltas = 0
    casaAtual = 0

    for _ in range(casasParaPassar):
        casaAtual += 1
        if casaAtual == tamanho:
            casaAtual = 0
            voltas += 1

    print(voltas, casaAtual)

if __name__ == "__main__":
    main()
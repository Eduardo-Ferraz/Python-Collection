# Faça um programa que leia um número inteiro n e então leia n linhas contendo
# informações sobre produtos separados por ponto-e-vírgula. Use funções de strings
# para:
# a. Remover os valores entre o primeiro e o segundo símbolo de ponto-e-vírgula;
# b. Converter o nome do produto para maiúsculo;
# c. Substituir “/home/” por “C:/Users/”.
# Mostre na tela os resultados das operações

def main():
    res = []
    n = int(input("Informe o numero de produtos: "))

    for i in range(n):
        arrayStr = input("Informe o produto: ").split(";")

        for j in range(2, len(arrayStr[i])):
            res.append(arrayStr[i])

    print(res)

if __name__ == '__main__':
    main()
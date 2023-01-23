# Faça um programa que leia um número inteiro n e então 
# leia n linhas contendo informações sobre produtos separados por ponto-e-vírgula. 
# Mostre na tela o número de produtos de cada categoria. 
# Assuma que as produtos podem ser escritas em diferentes casos (minúsculo, maiúsculo, etc.).

def main():
    n = int(input())
    produtos = []

    for i in range(n):
        produtos.append(input().split(';'))
        
        produtos[i][0] = produtos[i][0].upper()
        produtos[i].pop(1)
        produtos[i][3] = produtos[i][3].replace('/home/', 'C:/Users/')

        produtos[i] = ';'.join(produtos[i])

    for i in range(n):
        print(produtos[i])

if __name__ == '__main__':
    main()
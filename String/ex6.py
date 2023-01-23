# Faça um programa que leia um número inteiro n e então 
# leia n linhas contendo informações sobre produtos separados por ponto-e-vírgula. 
# Mostre na tela o número de produtos de cada categoria. 
# Assuma que as categorias podem ser escritas em diferentes casos (minúsculo, maiúsculo, etc.).

def main():
    check = 0
    categorias = []

    n = int(input())
        
    for i in range(n):
        cat = input().split(";")[1].lower()
        
        for j in range(len(categorias)):
            if cat == categorias[j][0]:
                categorias[j][1] += 1
                check = 1
                break

        if check == 0:
            categorias.append([f'{cat}', 1])

        check = 0

    for i in range(len(categorias)):
        print(f'{categorias[i][0]}: {categorias[i][1]}')
        
if __name__ == '__main__':
    main()
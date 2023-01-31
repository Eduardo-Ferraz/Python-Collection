# Faça um programa que leia um número inteiro n e então leia n linhas contendo o nome
# de um estudante e 4 números indicando as notas em 3 avaliações e o percentual de
# faltas. Mostre na tela os nomes dos aprovados assumindo que o critério de aprovação
# é ter nota média maior ou igual a 6 e percentual de faltas menor ou igual a 25%.

def main():
    strArray = []
    n = int(input())

    for i in range(n):
        strArray.append(input())

    for i in range(n):
        strArray[i] = strArray[i].split(" ")

        media = 0
        for j in range(1, 4):
            strArray[i][j] = int(strArray[i][j])
            media += strArray[i][j]

        media /= 3

        if media >= 6 and int(strArray[i][4]) <= 25:
            print(strArray[i][0])

if __name__ == '__main__':
    main()
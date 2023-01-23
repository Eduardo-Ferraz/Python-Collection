#  -> Faça um programa que leia um número inteiro n e, então, 
# leia n linhas, cada uma contendo as coordenadas de um vetor (números reais). 
#  -> Calcule a distância euclidiana entre os vetores e mostre na tela dois números 
# inteiros representando os índices dos vetores mais próximos, com o índice menor primeiro. 
#  -> Em caso de empate, retorne o par de índices que foi encontrado primeiro. 
# 
# A distância euclidiana é dada por:
# d(x, y) = raiz_quadrada( somatorio_i quadrado(xi - yi) )

import math

def calcDist(d, coord1, coord2):
    soma = 0
    for i in range(d):
        soma += math.pow(coord1[i] - coord2[i], 2)
    
    dist = math.sqrt(soma)
    return dist

def outrosPontos(index, totalPontos):
    lista = []
    for i in range(totalPontos):
        if i != index:
            lista.append(i)

    return lista
    
def main():
    indexMenorDist = -1
    menorDist = 999999
    n = int(input())
    linha = []
    distancias = []

    for _ in range(n):
        linha.append(input().split())

    dimensoes = len(linha[0])

    for j in range(n):
        for k in range(dimensoes):
            linha[j][k] = float(linha[j][k])

    for j in range(n):
        for m in outrosPontos(j, n):
            a = calcDist(dimensoes, linha[j], linha[m])
            if a < menorDist:
                menorDist = a
                distancias.append(a)
                indexMenorDist = f"{j} {m}"

    print(indexMenorDist)
    # print(dimensoes)
    # print(type(linha[0][0]))
    # print(linha)
    # print(distancias)

if __name__ == "__main__":
    main()
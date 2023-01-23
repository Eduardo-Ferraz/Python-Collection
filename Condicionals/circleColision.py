# Suponha que você está desenvolvendo um jogo 2D de tiro ao alvo e você deseja verificar se um tiro acertou o alvo. 
# Assuma que o tiro e o alvo são círculos e são conhecidas suas posições e raios. 
# Faça um programa que leia 6 números representando, nesta ordem, 
# as coordenadas x e y e o raio do primeiro círculo 
# e, em seguida, as mesmas informações sobre o segundo círculo, 
# e mostre na tela True se os círculos colidem e False caso contrário.

import math

def distancePoints(x1, y1, x2, y2):
    d = math.sqrt(math.pow(float(x1) - float(y1), 2) + math.pow(float(x2) - float(y2), 2))

    return d

def find_bigger(a, b):
    if a > b:
        return a

    return b

def main():
    circles = []

    for i in range(2):
        circles.append([])
        for _ in range(3):
            circles[i].append(float(input()))
    
    d = distancePoints(circles[0][0], circles[1][0], circles[0][1], circles[1][1])

    print(d < find_bigger(circles[0][2], circles[1][2]))

if __name__ == '__main__':
    main()
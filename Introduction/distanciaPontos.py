#Faça um programa que leia as coordenadas x e y de dois pontos 
# e mostre na tela a distância euclidiana entre eles com 1 casa após a vírgula. 
# A distância euclidiana é dada por d = sqrt( (x1 - x2)2 + (y1 - y2)2 ).

import math

def distancePoints(x1, y1, x2, y2):
    d = math.sqrt(math.pow(float(x1) - float(y1), 2) + math.pow(float(x2) - float(y2), 2))

    return d

def main():
    coord1 = input().split()
    coord2 = input().split()

    d = distancePoints(coord1[0], coord2[0], coord1[1], coord2[1])
    
    print(d)

if __name__ == '__main__':
    main()
# Em uma disciplina prática, o aluno é aprovado se 
# desenvolver um sistema ou se tirar mais de 60 pontos em uma prova e tiver 75% de presença ou mais. 
# Entrada: um número indicando se o sistema foi desenvolvido (1 se sim e 0 se não),
#  a nota da prova e a frequência. 
# Saída: True se o aluno foi aprovado e False caso contrário.

# Suponha que você está desenvolvendo um jogo 2D de tiro ao alvo e você deseja verificar se um tiro acertou o alvo. 
# Assuma que o tiro e o alvo são círculos e são conhecidas suas posições e raios. 
# Faça um programa que leia 6 números representando, nesta ordem, 
# as coordenadas x e y e o raio do primeiro círculo 
# e, em seguida, as mesmas informações sobre o segundo círculo, 
# e mostre na tela True se os círculos colidem e False caso contrário.

def main():
    data = []
    for _ in range(3):
        data.append(float(input()))
    
    aproved = data[0] == 1 or (data[1] > 60 and data[2] >= 75)

    print(aproved)
    
if __name__ == '__main__':
    main()
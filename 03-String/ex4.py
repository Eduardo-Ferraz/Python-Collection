# Faça um programa que leia uma linha contendo uma sequência de números separados
# por espaço e use funções de strings para exibir o dobro dos números na tela. 

def main():
    nbrs = input().split()
    
    for i in range(len(nbrs)):
        print(int(nbrs[i]) * 2) 

if __name__ == "__main__":
    main()
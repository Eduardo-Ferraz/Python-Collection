# Faça um programa que leia uma linha contendo uma sequência de números separados
# por espaço e use funções de strings para exibir o dobro dos números na tela. 

def main():
    #nbrs_str = input("Informe os numeros: ")
    nbrs_str = "789 4 7 41 -7 0 100"
    nbrs_int = []


    j = 0
    for i in range(len(nbrs_str)):
        if nbrs_str[i] == " ":
            if nbrs_str[i + 1] == "-":
                print("Caiu na rede é pexe")
                i+=1
                num_local = int(nbrs_str[slice(j, i)]) * -1
            else:
                num_local = int(nbrs_str[slice(j, i)])
            nbrs_int.append(num_local)
            j = i
            

    num_local = int(nbrs_str[slice(j, len(nbrs_str))])
    nbrs_int.append(num_local)
    print(nbrs_int)



if __name__ == "__main__":
    main()
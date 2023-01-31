# Faça uma função que use comandos de repetição para 
# implementar o slice indexing (sem usar esta funcionalidade).

def slice_index(L, start, end):
    L_ret = []
    for i in range(start, end):
        L_ret.append(L[i])
        
    return L_ret

def main():
    L = [3, 7, 0, 5, 1, 2, 19]

    print(slice_index(L, 2, 4)) # [0, 5]
    print(slice_index(L, 1, 6)) # [7, 0, 5, 1, 2]
    K = slice_index(L, 5, len(L))
    print(K) # [2, 19]

if __name__ == "__main__":
    main()
# Use comandos de repetição para implementar funções para buscar 
# o índice do maiorelemento e o índice do menor elemento de uma lista. 

def find_index_max(L):
    max = -99999
    for i in range(0, len(L)):
        if L[i] > max:
            max = L[i]
            i_max = i
    return i_max

def find_index_min(L):
    min = 99999
    for i in range(0, len(L)):
        if L[i] < min:
            min = L[i]
            i_min = i
    return i_min

def main():
    L = (3, 7, 0, 5, 1, 2, 19)

    print(find_index_max(L))
    print(find_index_min(L))

if __name__ == "__main__":
    main()
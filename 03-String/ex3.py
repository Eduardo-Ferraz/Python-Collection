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
    L = input().split()

    for i in range(len(L)):
        L[i] = float(L[i])

    print(find_index_min(L))
    print(find_index_max(L))

if __name__ == "__main__":
    main()
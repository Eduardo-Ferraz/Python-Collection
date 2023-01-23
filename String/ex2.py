# Use comandos de repetição para implementar funções para 
# buscar o mínimo, máximo, soma e média de uma lista ou tupla.

def find_max(L):
    max = -99999
    for i in range(0, len(L)):
        if L[i] > max:
            max = L[i]
    return max

def find_min(L):
    min = 99999
    for i in range(0, len(L)):
        if L[i] < min:
            min = L[i]
    return min

def find_soma(L):
    soma = 0
    for i in range(0, len(L)):
        soma += L[i]

    return soma

def find_med(L):
    med = find_soma(L) / len(L)

    return med

def main():
    L = []
    n = int(input())

    for _ in range(n):
        L.append(float(input()))

    print(f"{find_min(L):.2f}")
    print(f"{find_max(L):.2f}")
    print(f"{find_soma(L):.2f}")

if __name__ == "__main__":
    main()
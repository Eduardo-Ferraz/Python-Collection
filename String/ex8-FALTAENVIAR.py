# Neste exercício você criará uma função para ordenar uma lista de elementos. 
# Não é permitido usar funções prontas (e.g., sorted ou sort) para resolver esta questão. 
# Devem ser implementadas as seguintes funções:

# 1) Uma função que receba uma lista e um número inteiro i e 
# coloque na posição i o menor elemento encontrado entre as posições i a n, 
# onde n é o tamanho da lista.

# 2) Uma função que receba a lista e a ordene. 
# A função deve usar a função acima para colocar o menor elemento na posição 0, 
# o segundo menor na posição 1, o terceiro menor na posição 2 e assim por diante. 
# Este algoritmo de ordenação é chamado de ordenação por seleção.

def tradeFrom(lista, i):
    menor = lista[i]
    indexMenor = i

    for j in range(i, len(lista)):
        if lista[j] < menor:
            menor = lista[j]
            indexMenor = j
        
    hold = lista[i]
    lista[i] = lista[indexMenor]
    lista[indexMenor] = hold

def orderList(lista):
    for i in range(len(lista)):
        tradeFrom(lista, i)

def main():
    lista = input().split()

    for e in range(len(lista)): 
        lista[e] = float(lista[e])

    orderList(lista)
    
    for e in range(len(lista)): 
        lista[e] = str(lista[e])

    lista = '0 '.join(lista) + '0'

    print(lista)
if __name__ == '__main__':
    main()
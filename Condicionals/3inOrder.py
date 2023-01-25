# Leia 3 números inteiros e mostre-os em ordem na tela usando apenas condicionais.

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
    lista = []
    for _ in range(3):
        lista.append(int(input())) 

    orderList(lista)
    
    for e in range(len(lista)): 
        lista[e] = str(lista[e])

    lista = ' '.join(lista)

    print(lista)
if __name__ == '__main__':
    main()
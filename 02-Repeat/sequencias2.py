# Escreva programas que leiam um número inteiro n e mostrem na tela os n primeiros números das sequências abaixo.

# 0, 1, 2, 3, 4, 5
# 5, 4, 3, 2, 1, 0
# 7, 9, 11, 13, 15, 17, 19
# 21, 18, 15, 12, 9

def main():
    seq=[[], [], [], []]
    n = int(input())

    for i in range(n):
        seq[0].append(str(i))
        seq[1].append(str(5 - i))
        seq[2].append(str(7 + 2 * i))
        seq[3].append(str(21 - 3 * i))

    for i in range(4):
        print(', '.join(seq[i]))

if __name__ == '__main__':
    main()
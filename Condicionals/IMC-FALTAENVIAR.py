# Faça um programa que leia a altura (em metros) o peso (em Kg) de uma pessoa, 
# calcule seu IMC e mostre na tela em qual categoria ela se encontra. 
# O IMC é dado pela divisão do peso pela altura ao quadrado. 
# As categorias são:

# IMC (kg/m2) Categoria
# 18,5 - 24,99 Normal
# 25 - 29,99 Pré-obeso
# 30 - 34,99 Obesidade classe I
# 35 - 39,99 Obesidade classe II

def main():
    h = float(input())
    w = float(input())

    imc = w / h ** 2

    if imc < 25:
        print('Normal')
    elif imc < 30:
        print('Pré-obeso')
    elif imc < 35:
        print('Obesidade classe I')
    else:
        print('Obesidade classe II')
    
if __name__ == '__main__':
    main()
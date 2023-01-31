# # Crie uma classe Circulo que tenha como atributo o raio 
# e uma classe Retangulo que tenha como atributos a largura e altura. 
# Crie um construtor que receba o valor dos atributos e métodos área e perímetro.

# Escreva uma função main que leia um número inteiro n e, em seguida, 
# leia os dados de n formas (formas são retângulos ou círculos). 
# A primeira letra da linha indica se os dados são de um circulo (C) ou retângulo (R). 
# Para cada linha, crie um objeto do tipo definido pela letra e adicione o objeto em uma lista.

# Ao final, mostre na tela a soma das áreas e dos perímetros das formas, nesta ordem, 
# com 1 casa depois da vírgula. A área e perímetro de cada forma deve ser calculada 
# usando os métodos da classe. Na questão, assuma PI=3.1415.

# IMPORTANTE: Existem formas mais simples de resolver a questão, 
# mas as operações devem ser feitas como especificado. 
# O objetivo da questão é avaliar a capacidade do aluno de criar classes e objetos, 
# e de manipular listas de objetos.

PI = 3.1415

class Circulo:
    def __init__(self, r) -> None:
        self.raio = r

    def area(self):
        self.area = PI * self.raio ** 2
        return self.area

    def perimetro(self):
        self.perimetro = 2 * PI * self.raio
        return self.perimetro

class Retangulo:
    def __init__(self, larg, alt) -> None:
        self.larg = larg
        self.alt = alt

    def area(self):
        self.area = self.larg * self.alt
        return self.area

    def perimetro(self):
        self.perimetro = 2 * (self.larg + self.alt)
        return self.perimetro

def main():
    list = []
    areaTotal = perTotal = 0

    n = int(input())

    for i in range(n):
        receive = input().split()

        if receive[0] == 'C':
            obj = Circulo(float(receive[1]))
        elif receive[0] == 'R':
            obj = Retangulo(float(receive[1]), float(receive[2]))
        

        list.append(obj)

    for i in range(len(list)):
        perTotal += list[i].perimetro()
        areaTotal += list[i].area()

    print(f'{areaTotal:.1f} {perTotal:.1f}')

if __name__ == "__main__":
    main()
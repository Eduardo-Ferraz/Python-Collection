# # Escreva uma classe Funcionário que tenha como atributos 
# o nome do funcionário, o salário-base, o número de atendimentos realizados no mês, 
# e a titulação (técnico, graduação, mestrado ou doutorado). 
# Na classe, crie os métodos:

# a. __init__: o construtor deve receber os valores dos atributos.

# b. __str__: deve retornar uma string no formato 
# “Funcionario(nome, salario_base=valor, n_atendimentos=valor, titulação=valor)”.

# c. salario: deve retornar o salário total do funcionário que é dado pela soma do salário-base, 
# mais R$25 por atendimento e um bônus por titulação dado pelo produto do salário de base por um 
# multiplicador dependente da titulação, sendo 1.0 para técnico, 2.0 para graduação, 5.0 para mestrado e 10 para doutorado.

# Faça uma função main que leia uma linha contendo, respectivamente, 
# o nome, salário-base, número de atendimentos e titulação de um funcionário, 
# use os dados para criar um objeto do tipo Funcionario 
# e mostre na tela uma mensagem informando o salário total do funcionário com duas casas decimais. 
# Assuma que as titulações serão digitadas sem acento.

class Funcionario:
    def __init__(self, n, s, a, t) -> None:
        self.nome = n
        self.salBase = s
        self.numAtend = a
        self.titul = t

    def __str__(self) -> str:
        return 'Funcionario(nome, salario_base=valor, n_atendimentos=valor, titulação=valor)'

    def salario(self) -> float:
        multiplicador = {
            'tecnico': 1.0,
            'graduacao': 2.0,
            'mestrado': 5.0,
            'doutorado': 10.0,
        }

        bonusTitul = self.salBase * multiplicador[self.titul]

        salTotal = self.salBase + 25 * self.numAtend + bonusTitul

        return salTotal

def main():
    texto = input().split()
    texto[1] = float(texto[1])
    texto[2] = float(texto[2])

    func = Funcionario(texto[0], texto[1], texto[2], texto[3])

    print(f'Salario de {func.nome}: {func.salario():.2f}')

if __name__ == "__main__":
    main()
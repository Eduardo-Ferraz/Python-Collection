# Se for escolhida a opção 1, o programa deve exibir a mensagem “Bom dia!” na tela.
# Se for escolhida a opção 2, o programa deve exibir “Sem perspectiva de chuva.”.
# Se for escolhida a opção 0, o programa deve ser encerrado.

# Se qualquer outro valor for digitado, o programa deve exibir a mensagem “Opção inválida.”.

def message(escolha) -> None:
    opcoes = {
            1: 'Bom dia!',
            2: 'Sem perspectiva de chuva.',
        }
    print(opcoes[escolha])

def main():
    while True:
        escolha = int(input())
        
        if escolha == 0:
            break
        elif escolha > 2 or escolha < 0:
            print('Opção inválida.')
        else:
            message(escolha)

if __name__ == "__main__":
    main()
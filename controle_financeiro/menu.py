

def exibir_menu():
    print("\n*******************************")
    print("Sistema de Controle Financeiro")
    print("*******************************")
    print("1 - Adicionar receita\n"
          "2 - Adicionar despesa\n"
          "3 - Listar movimentações\n"
          "4 - Mostrar o saldo\n"
          "5 - Sair do Sistema")
    try:
        opcao = int(input("Digite a opção desejada: "))
        if 1 <= opcao <= 5:
            return opcao
        else:
            print('Opção inválida! Escolha um número entre 1 e 5')
    except ValueError:
        print('Entrada inválida! Digite um número entre 1 e 5')

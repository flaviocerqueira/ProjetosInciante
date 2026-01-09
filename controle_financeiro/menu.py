

def exibir_menu():
    print("\n*******************************")
    print("Sistema de Controle Financeiro")
    print("*******************************")
    print('1 - Adicionar receita\n'
          '2 - Adicionar despesa\n'
          '3 - Listar movimentações\n'
          '4 - Mostrar o saldo\n'
          '5 - Sair do Sistema')
    opcao = int(input('Digite a opção desejada: '))
    return opcao


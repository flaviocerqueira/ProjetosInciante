import menu
from dados import movimentacoes
from operacoes import adicionar_receita, adicionar_despesa

if __name__ == "__main__":
    while True:
        opcao = menu.exibir_menu()
        if opcao == 1:
            movimentacoes.append(adicionar_receita())
            print(movimentacoes)
        elif opcao == 2:
            movimentacoes.append(adicionar_despesa())
            print(movimentacoes)
        elif opcao == 3:
            print('Funcionalidade em desenvolvimento')
        elif opcao == 4:
            print('Funcionalidade em desenvolvimento')
        elif opcao == 5:
            print('SISTEMA FINALIZADO')
            break


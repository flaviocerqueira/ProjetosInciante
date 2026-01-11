import menu
from dados import movimentacoes
from operacoes import adicionar_receita, adicionar_despesa, listar_movimentacoes, calcular_saldo

if __name__ == "__main__":
    while True:
        opcao = menu.exibir_menu()
        if opcao == 1:
            movimentacoes.append(adicionar_receita())
        elif opcao == 2:
            movimentacoes.append(adicionar_despesa())
        elif opcao == 3:
            listar_movimentacoes(movimentacoes)
        elif opcao == 4:
            print(calcular_saldo(movimentacoes))
        elif opcao == 5:
            print('SISTEMA FINALIZADO')
            break


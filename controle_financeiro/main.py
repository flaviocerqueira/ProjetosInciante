import menu
from dados import carregar_dados, salvar_dados
from operacoes import adicionar_receita, adicionar_despesa, listar_movimentacoes, calcular_saldo

movimentacoes = carregar_dados()

if __name__ == "__main__":
    while True:
        opcao = menu.exibir_menu()
        if opcao == 1:
            movimentacoes.append(adicionar_receita())
            salvar_dados(movimentacoes)
        elif opcao == 2:
            movimentacoes.append(adicionar_despesa())
            salvar_dados(movimentacoes)
        elif opcao == 3:
            listar_movimentacoes(movimentacoes)
        elif opcao == 4:
            print(f'Saldo Atual: R$ {calcular_saldo(movimentacoes):.2f}')
        elif opcao == 5:
            print('SISTEMA FINALIZADO')
            break

TIPO_RECEITA = 'RECEITA'
TIPO_DESPESA = 'DESPESA'


def adicionar_receita():
    categoria = input("Qual a categoria da Receita? ")
    valor = validar_valor()
    return {
            'tipo': TIPO_RECEITA,
            'categoria': categoria,
            'valor': valor
    }


def adicionar_despesa():
    categoria = input("Qual a categoria da Despesa? ")
    valor = validar_valor()
    return {
        'tipo': TIPO_DESPESA,
        'categoria': categoria,
        'valor': valor
    }


def calcular_saldo(movimentacoes):
    saldo = 0

    for movimento in movimentacoes:
        if movimento['tipo'] == TIPO_RECEITA:
           saldo += movimento['valor']
        elif movimento['tipo'] == TIPO_DESPESA:
            saldo -= movimento['valor']
    return saldo


def listar_movimentacoes(movimentacoes):
    for movimento in movimentacoes:
        print(f"[{movimento['tipo']}] {movimento['categoria']} - R$ {movimento['valor']:.2f}")


def validar_valor():
    while True:
        try:
            valor = float(input('Informe o valor: '))
            if valor >= 0:
                print('Entrada cadastrada.')
                return valor
            else:
                print('Entrada inválida. Informe um valor positivo!')
        except ValueError:
            print('Entrada inválida. Informe um valor numérico')
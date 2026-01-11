from datetime import datetime

TIPO_RECEITA = 'RECEITA'
TIPO_DESPESA = 'DESPESA'


def adicionar_receita():
    categoria = input("Qual a categoria da Receita? ")
    valor = validar_valor()
    data = validar_data()
    return {
            'tipo': TIPO_RECEITA,
            'categoria': categoria,
            'valor': valor,
            'data': data
    }


def adicionar_despesa():
    categoria = input("Qual a categoria da Despesa? ")
    valor = validar_valor()
    data = validar_data()
    return {
        'tipo': TIPO_DESPESA,
        'categoria': categoria,
        'valor': valor,
        'data': data
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
        print(
            f"[{movimento['tipo']}] "
            f"{movimento['categoria']:<15} "
            f"R$ {movimento['valor']:>8.2f} "
            f"{movimento['data']}"
        )


def validar_valor():
    while True:
        try:
            valor = float(input('Informe o valor: '))
            if valor >= 0:
                return valor
            else:
                print('Entrada inválida. Informe um valor positivo!')
        except ValueError:
            print('Entrada inválida. Informe um valor numérico')


def validar_data():
    while True:
        try:
            data_str = input('Informe a data da movimentação financeira (DD/MM/AAAA): ')
            data_obj = datetime.strptime(data_str, '%d/%m/%Y')
            return data_obj.strftime('%d/%m/%Y')
        except ValueError:
            print('Formato de data inválido. Por favor, use o formato DD/MM/AAAA')


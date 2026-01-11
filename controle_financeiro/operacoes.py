

def adicionar_receita():
    categoria = input("Qual a categoria da Receita? ")
    valor = float(input("Qual o valor da Receita? "))
    return {
            'tipo': 'RECEITA',
            'categoria': categoria,
            'valor': valor
    }


def adicionar_despesa():
    categoria = input("Qual a categoria da Despesa? ")
    valor = float(input("Qual o valor da Despesa? "))
    return {
        'tipo': 'DESPESA',
        'categoria': categoria,
        'valor': valor
    }


def calcular_saldo(movimentacoes):
    saldo = 0
    for movimento in movimentacoes:
        if movimento['tipo'] == 'RECEITA':
           saldo += movimento['valor']
        elif movimento['tipo'] == 'DESPESA':
            saldo -= movimento['valor']
    return saldo


def listar_movimentacoes(movimentacoes):
    for movimento in movimentacoes:
        print(f"[{movimento['tipo']}] {movimento['categoria']} - R$ {movimento['valor']}")


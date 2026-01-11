

def adicionar_receita():
    categoria = input("Qual a categoria da Receita? ")
    valor = float(input("Qual o valor da Receita? "))
    return {
            'tipo': 'receita',
            'categoria': categoria,
            'valor': valor
    }


def adicionar_despesa():
    categoria = input("Qual a categoria da Despesa? ")
    valor = float(input("Qual o valor da Despesa? "))
    return {
        'tipo': 'despesa',
        'categoria': categoria,
        'valor': valor
    }


def calcular_saldo():
    pass


def listar_movimentacoes():
    pass


import json

ARQUIVO_DADOS = 'movimentacoes.json'


def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


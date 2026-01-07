import random


def sortear_numero():
    return random.randint(1,3)


def chutar_numero(segredo):

    tentativas = 3
    chutes = []

    for i in range(tentativas):
        chute = int(input("Digite um numero entre 1 e 1000: "))
        if chute == segredo:
            print(f'Parabéns. Você acertou! O número secreto é {segredo}')
            break
        else:
            print('Você errou. Tente novamente!')
            chutes.append(chute)
            tentativas -= 1

    if tentativas == 0:
        print(f'Você chutou os números {chutes} e o número secreto é {segredo}')


chave = sortear_numero()
chutar_numero(chave)


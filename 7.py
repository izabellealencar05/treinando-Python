# Escreva um programa que simule o jogo da forca.
# O programa deve escolher uma palavra aleatória e
# permitir que o usuário adivinhe as letras. O jogo deve
# exibir na tela a palavra com as letras adivinhadas
# corretamente e informar quantas tentativas o usuário ainda tem.
import random


def palavraaleatoria():
    listapalavras = ["python", "programacao", 'clara', 'ciencia', 'cientista', 'familia', 'estudos']
    palavra = random.choice(listapalavras)
    return palavra
def exibir(palavra, letrascorretas):
    exibicao = ""
    for letra in palavra:
        if letra in letrascorretas:
            exibicao += letra + ""
        else:
            exibicao += "-"
    return exibicao
def jogodaforca ():
    palavra = escolherpalavra
    letrascorretas = []
    tentativas = 6
    print('bem vindo ao jogo da forca!')
    print('adivinhe a palavra! Boa sorte!')

    while True:
        print('\nPalavra: ', +exibir(palavra, letrascorretas))
        print('tentativas restantes: ', +str(tentativas))

        if tentativas == 0:
            print("\nVocê perdeu! A palavra correta era: " +palavra)
            break

        if "_" not in exibir(palavra, letrascorretas):
            print("\nParabéns! Você venceu!")
            break

        letra = input("Digite uma letra: ")

        if letra in letrascorretas:
            print("Você já adivinhou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letrascorretas.append(letra)
            print("Adivinhação correta!")
        else:
            tentativas -= 1
            print("Adivinhação incorreta!")

jogodaforca()
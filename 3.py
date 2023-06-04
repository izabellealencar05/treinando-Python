# Escreva um programa que leia uma frase do usuário e conte
# quantas vezes cada palavra aparece. Em seguida, exiba na
# tela a contagem de cada palavra.

x = str(input('digite uma frase: '))
palavras = x.split()
qntdpalavras = len(palavras)
print('a quantidade de palavras nessa frase é: ', qntdpalavras)
# Escreva um programa que peça ao usuário para digitar um número inteiro e, em seguida, exiba na tela se o número é par ou ímpar.

x = int(input('digite um numero: '))

if x % 2 == 0:
    print('o numero', x, 'é par')
else:
    print('o número', x,  'é ímpar')
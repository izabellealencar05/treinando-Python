# Escreva um programa que leia uma lista de números e
# encontre o maior e o menor número da lista. Em seguida,
# exiba na tela esses valores.

lista = []
x = int(input('escreva a quantidade de elementos: '))
for i in range (x):
    y = int(input('digite um numero: '))
    lista.append(y)
print(lista)
print('o menor numero da lista é', min(lista))
print('o maior numero da lista é', max(lista))
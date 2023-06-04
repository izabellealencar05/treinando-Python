# Escreva uma função que receba uma lista como argumento e retorne
# uma nova lista contendo apenas os elementos pares da lista original.

listaimpares = []
lista = []
y = int(input('quantas elementos? '))
for i in range(y):
    x = int(input('digite um numero: '))
    lista.append(x)
    if x%2 != 0:
        listaimpares.append(x)
print('lista original', lista)
print('lista so de pares', listaimpares)
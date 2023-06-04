# faça um programa que tenha funcao chamada area que receba as
# deminesoes de um terreo reteangular e mostre a atrea do terreno

def area (comprimento, largura):
    a = largura*comprimento
    print("a area do terreno é: ", a)



c = float(input('digite o comprimento: '))
l = float(input('digite a largura: '))
area(c, l)

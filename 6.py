# Escreva uma função que receba uma lista de palavras como
# argumento e retorne uma nova lista contendo apenas as palavras
# que são palíndromos (ou seja, lidas da mesma forma de trás para frente).

def palindromos(lista_palavras):
    palindromos = []
    for palavra in lista_palavras:
        if palavra == palavra[::-1]:
            palindromos.append(palavra)
    return palindromos


lista_palavras = ["arara", "python", "radar", "casa", "ana"]
palindromos_lista = palindromos(lista_palavras)
print("lista de palindromos: ", palindromos_lista)
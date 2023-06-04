# faca um programa que tenha uma funcao chamada escreva(),
# que receba um texto qualquer como parametro e mostra a
# mensagem com tamanho adaptavel

def escreva(msg):
    tan = len(msg)
    print('~' * tan)
    print(f'{msg}')
    print('~' * tan)


escreva('izabelle')
escreva('iza')
escreva('victor hugo')
escreva('waldemar')
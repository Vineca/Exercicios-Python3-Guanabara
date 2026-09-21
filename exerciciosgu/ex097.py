def escreva(txt):
    largura = len(txt) + 4
    print('-' * largura)
    print(f'{txt:^{largura}}')
    print('-' * largura)


escreva('Vinicius')
escreva('esses exercicios estão muito faceis gustavin')
escreva('Professor fuleiro de fuleirage')
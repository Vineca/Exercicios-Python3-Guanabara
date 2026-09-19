numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero: '))
saida = 0
while saida != 5:
    saida = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual comando deseja:'''))
    if saida == 1:
        print('{} + {} = {}'.format(numero1, numero2, numero1 + numero2))
    elif saida == 2:
        print('{} * {} = {}'.format(numero1, numero2, numero1 * numero2))
    elif saida == 3:
        print('O maior numero é: {}'.format(numero1 if numero1 > numero2 else
                                           numero2 if numero1 < numero2 else
                                           'nenhum, eles são iguais'))
    elif saida == 4:
        numero1 = int(input('Novo primeiro numero: '))
        numero2 = int(input('Novo segundo numero: '))
while True:
    num = int(input('Quer ver a tabuada de qual numero: '))
    cont = 0
    if num < 0: break
    while cont < 10:
        cont += 1
        print(f'{num} x {cont} = {num * cont}')
def contador(i, f, p):
    while True:
        if (i <= f and p > 0) or (i >= f and p < 0):
            for c in range(i, (f+1) if p> 0 else (f-1), p):
                print(c)
            break
        else:
            print('Tente de novo')
            i = int(input('inicio: '))
            f = int(input('fim: ')) 
            p = int(input('passo: '))



contador(1, 10, 1)
print('FIM')
contador(10, 0, -2)
print('FIM')
contador(int(input('inicio: ')), int(input('fim: ')), int(input('passo: ')))
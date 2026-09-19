x = int(input('Digite um numero qualquer:'))
fatorial = 1
while x > 0:
    print('{} '.format(x), end='')
    if x > 1 : print('X ', end='')
    fatorial *= x
    x = x - 1
print('=',fatorial)
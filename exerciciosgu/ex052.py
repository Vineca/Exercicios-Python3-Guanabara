numero = int(input('digite um numero: '))
s = 0
for c in range(1,numero+1):
    if numero % c == 0: s += 1
if s == 2: print(numero, 'primo')
else: print(numero, 'não é primo')
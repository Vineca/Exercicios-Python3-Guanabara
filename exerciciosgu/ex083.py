a = list(input('Manda la expression: '))
b = a[:]
validade = 0
d = 0
for posi,letra in enumerate(a):
    if letra == ')':
        for c in range(posi+d,-1,-1):
            if b[c] == '(':
                b.pop(c)
                d -= 1
                break
            if c == 0:
                validade += 1
                break
if '(' in b:
    validade += 1

if validade == 0: print('deu noia')
else: print('fudeu noia')







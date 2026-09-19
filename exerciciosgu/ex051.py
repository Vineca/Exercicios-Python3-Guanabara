t = int(input('digite qual o primeiro termo: '))
r = int(input('digite qual a razao: '))
if r == 0:
    for c in range(0,10):
        print(t)
else:
    for c in range(t,(r*10)+t,r):
        print(c)
t = int(input('digite qual o primeiro termo: '))
r = int(input('digite qual a razao: '))
g = t
if r != 0:
    while t != ((r*10)+g):
        print(t)
        t = t + r
else:
    print((str(t)+' ')*10)

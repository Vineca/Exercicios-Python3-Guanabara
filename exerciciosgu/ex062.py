t = int(input('digite qual o primeiro termo: '))
r = int(input('digite qual a razao: '))
g = t
if r != 0:
    while t != ((r*10)+g):
        print(t)
        t = t + r
else:
    print((str(t)+' ')*10)
mais = int(input('Mais quantas repetições você quer: '))
contagem = 10
while mais != 0:
        print(t)
        t = t + r
        mais -= 1
        contagem += 1
        if mais == 0:
            mais = int(input('Mais quantas repetições você quer: '))
print('Foram contados', contagem    )
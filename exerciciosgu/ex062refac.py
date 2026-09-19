t = int(input('digite qual o primeiro termo: '))
r = int(input('digite qual a razao: '))
g = t
cont = 0
mais = 10
while mais != 0:
    print(g)
    g = g + r
    cont += 1
    mais -= 1
    if mais == 0 : mais = int(input('digite quantas repetição mais vossa senhoria deseja? '))
print(f'Contagem ai malandro = {cont}')
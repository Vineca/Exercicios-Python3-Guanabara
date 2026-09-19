import random
x = int(input('Quantos jogos vc manda chefe?'))
lista = []
for c in range(x):
    lista.append([])

for jogo in lista:
    while len(jogo) < 6:
        a = random.randint(1,60)
        if a not in jogo:
            jogo.append(a)
    print(jogo)
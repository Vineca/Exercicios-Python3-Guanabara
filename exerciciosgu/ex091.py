from random import randint
from time import sleep
dicionario = dict()
for c in range(0, 4):
    dicionario[c+1] = randint(1, 6)
    print(f'jogador {c+1} tirou {dicionario[c+1]} no dado')
    # sleep(1)
ordem = dict()
while len(ordem) < 4:
    for jog,dado in dicionario.items():
      if max(dicionario.values()) == dado :
        # ordem.append(dicionario[jog])
        ordem[jog] = dado
        del(dicionario[jog])
        break
print()
print()

for l, (c,v) in enumerate(ordem.items(), start=1):
    print(f' Em {l} ficou Jogador {c} com {v} no dado')


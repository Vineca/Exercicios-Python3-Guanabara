quatro = (int(input('Digite um numero: ')),
            int(input('Digite mais um numero: ')),
            int(input('Digite mais um numero: ')),
            int(input('Digite o ultimo numero: ')))
print(quatro.count(9))

if 3 in quatro : print(quatro.index(3))
else: print('Gostando de mamar ein!')
par = 0
for numero in quatro:
    if numero % 2 == 0:
        par += 1
print(par)
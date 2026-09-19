lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N': break
print(len(lista))
print((sorted(lista, reverse=True)))
if 5 in lista:
    print('ta sim chefe')
else: print('nao ta chefe')
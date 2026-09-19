lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = (input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N': break
par = list()
impar = list()
for num in lista:
    if num % 2 == 0: par.append(num)
    else:
        impar.append(num)
print(lista)
print()
print(par)
print()
print(impar)

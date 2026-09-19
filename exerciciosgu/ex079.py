lista = [int(input('Digite um valor: '))]
continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
novo = 0
while continuar not in 'N':
    novo = (int(input('Digite um valor: ')))
    if novo not in lista:
        lista.append(novo)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print(sorted(lista))

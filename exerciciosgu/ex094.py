lista = list()
continuar = 'S'
totidade = 0
while continuar != 'N':
    dicionario = {}
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dicionario['idade'] = int(input('Idade: '))
    totidade += dicionario['idade']
    lista.append(dicionario.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print(len(lista))
print(totidade/len(lista))
print('Mulheres: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print()
print('Pessoas com idade acima da média: ', end='')
for i in lista:
    if i['idade'] > (totidade/len(lista)):
        print(i['nome'],',', end='')


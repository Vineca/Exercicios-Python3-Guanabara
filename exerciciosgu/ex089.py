lista = []
contagem = 0
while True:
    lista.append([(input('Digite nome do aluno: '))])
    lista[contagem].append([int(input('Qual sua primeira nota ?'))])
    lista[contagem][1].append(int(input('Qual sua segunda nota ? ')))
    contagem += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N': break
print(lista)
for boletim in lista:
    print(boletim[0], end = '')
    print(' sua media é: ',(boletim[1][0]+boletim[1][1])/2)
while True:
    qual = int(input('Quer saber a nota de quem kraio ou 999?'))-1
    if qual == 998: break
    print(lista[qual][0],' Média do burrinho: ', end = '')
    print(lista[qual][1])
    
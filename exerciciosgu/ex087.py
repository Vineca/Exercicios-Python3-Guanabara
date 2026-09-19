linhas = [[], [], []]
for linha in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor da linha ({linha},{c}): '))
        linhas[linha].append(num)
soma3 = 0
somapares = 0
for linha in linhas:
    print(linha)
    soma3  += linha[2]
    for num in linha:
        if num % 2 == 0:
            somapares += num

print()
print(max(linhas[1]))
print(f'Os pares somam {somapares}')
print(f'A soma da 3 coluna {soma3}')
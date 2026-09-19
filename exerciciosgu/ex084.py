cadastro = list()
dados = []
pesado = []
leve = []
cont = 0
while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(float(input('Digite um peso: ')))
    cadastro.append(dados[:])
    if len(cadastro) == 1 :
        pesado.append(dados[:])
        leve.append(dados[:])
    else:
            if pesado[0][1] < dados[1] :
                pesado.clear()
                pesado.append(dados[:])
            elif pesado[0][1] == dados[1]:
                pesado.append(dados[:])
            if leve[0][1] > dados[1] :
                leve.clear()
                leve.append(dados[:])
            elif leve[0][1] == dados[1] :
                leve.append(dados[:])
    dados.clear()
    a = input('Quer continuar [S/N] ?').upper().strip()[0]
    if a == 'N': break

print(len(cadastro))
print(f'Lista dos gordin, pesando {pesado[0][1]} pessoas: ')
for nome in pesado:
    print(nome[0])
print(f'Lista dos magrin, pesando {leve[0][1]} pessoas: ')
for nome in leve:
    print(nome[0])

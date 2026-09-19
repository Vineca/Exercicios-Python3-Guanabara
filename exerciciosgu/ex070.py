total = produtos = cont = 0
while True:
    nome = input('Qual seu produto? ')
    preço = float(input('Qual o preço do produto? '))
    continuar = input('Quer continuar? [S/N] ')
    total += preço
    if preço > 1000 : produtos += 1
    if cont == 0 : menor = nome,preço
    elif menor[1] > preço : menor = nome,preço
    cont += 1
    if continuar in 'Nn' :
        break
print(total)
print(produtos)
print(menor[0])
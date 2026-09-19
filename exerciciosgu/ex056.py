idade = 0,''
media = 0
sexo = 0
for c in range(1, 5):
    a1 = input('Digite seu nome: ')
    b2 = input('Digite seu sexo: ').upper()
    d3 = int(input('Digite sua idade: '))
    media += d3
    if d3 > idade[0] and b2 == 'MASC' : idade = d3,a1
    if d3 < 20 and b2 == 'FEM' : sexo += 1
print('O homem mais velho é:',idade[1])
print('A media de idades é',media/4)
print('Existem {} do sexo feminino'.format(sexo))
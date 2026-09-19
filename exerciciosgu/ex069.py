homi = muie = maior = 0
while True:
    nome = input('Qual seu nome? ')
    idade = int(input('Qual a idade? '))
    sexo = input('Qual o sexo? [F/M] ')
    continuar = input('Deseja continuar? [S/N] ')
    if sexo in 'Ff' and idade < 20:
        muie += 1
    if sexo in 'Mm' :
        homi += 1
    if idade > 18:
        maior += 1
    if continuar in 'Nn': break
print(homi)
print(maior)
print(muie)
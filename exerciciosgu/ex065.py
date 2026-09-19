menor = 0
maior = 0
soma = 0
c = 'S'
contagem = 0
while c != 'N':
    numero = int(input('Digite um numero inteiro: '))
    soma += numero
    if contagem == 0 : menor = maior = numero
    if numero > maior: maior = numero
    elif numero < menor: menor = numero
    c = str(input('Quer continuar? [S/N] ')).upper()
    contagem += 1
print(maior)
print(menor)
print(soma/contagem)
numero1 = int(input('Digite 1 numero: '))
numero2 = int(input('Digite 2 numero: '))
numero3 = int(input('Digite 3 numero: '))
maior = numero1
menor = numero2
if maior < numero2 : maior = numero2
if maior < numero3 : maior = numero3
if menor > numero1 : menor = numero1
if menor > numero3 : menor = numero3
print('O maior numero é: {}'.format(maior))
print('O menor numero é: {}'.format(menor))

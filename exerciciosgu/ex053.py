frase = str(input('Digite uma frase: ')).strip().upper()
palin = ''
frase = frase.replace(' ','')
for c in range(len(frase)-1,-1,-1):
    palin += frase[c]

print('A frase {} palindromo'.format('não é' if palin != frase else 'é'))


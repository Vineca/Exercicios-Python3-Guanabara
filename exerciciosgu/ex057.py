sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual seu sexo [M/F] :').upper()
    if sexo != 'M' and sexo != 'F' :
        print('Sexo incorreto')
    else:
        print('Sexo feito com sucesso')
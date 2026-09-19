from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
alistamento = 'é este'
if idade < 18 : alistamento = 'é em {}'.format((18 - idade))
elif idade > 18 : alistamento = 'foi há {}'.format(-(18 - idade))
print('Seu alistamento {} {}'.format(alistamento,'anos' if abs(18-idade)>1 else 'ano'))
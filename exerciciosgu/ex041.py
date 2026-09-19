ano = int(input('Digite o ano de nascimento: '))
from datetime import date
idade = date.today().year - ano
if idade <= 9: categoria = 'MIRIM'
elif idade <= 14 : categoria = 'INFANTIL'
elif idade <= 19 : categoria = 'JUNIOR'
elif idade <= 25 : categoria = 'SENIOR'
else: categoria = 'MASTER'
print('Sua categoria é',categoria)

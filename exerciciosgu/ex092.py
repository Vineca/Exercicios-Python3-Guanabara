trabalhador = {}
from datetime import date

trabalhador['nome'] = str(input('Nome: '))
trabalhador['Ano'] = int(input('Ano de nascimento: '))
trabalhador['CTPS'] = int(input('Carteira de trabalho: '))
trabalhador['Idade'] = date.today().year - trabalhador['Ano']
if trabalhador['CTPS'] != 0:
    trabalhador['contratado'] = int(input('Em que ano foi contratado: '))
    trabalhador['salario'] = int(input('Qual salario: '))
    trabalhador['aposentadoria'] = (35 + trabalhador['contratado']) - trabalhador['Ano']
print(trabalhador)

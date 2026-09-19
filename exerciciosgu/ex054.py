from datetime import date
maioridade = 0
menoridade = 0
for c in range(1,8):
    ano = input('{} Ano de nascimento: '.format(c))
    idade = date.today().year - int(ano)
    if idade >= 21 : maioridade += 1
    else : menoridade += 1
print('{} atingiram a maioridade'.format(maioridade))
print('{} ainda não atingiram a maioridade'.format(menoridade))

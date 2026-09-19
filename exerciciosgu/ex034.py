salario = float(input('Qual o seu salario: '))
print('Seu aumento é de: {:.2f}'.format(salario*0.1 if salario > 1250 else salario*0.15))
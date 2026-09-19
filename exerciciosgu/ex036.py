valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salario'))
tempo = int(input('Quantos anos deseja pagar: '))

if 0.3*salario >= (valor/(tempo*12)) : print('O emprestimo está disponivel')
else:
    print('O emprestimo foi negado')
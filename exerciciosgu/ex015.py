km = float(input('Qual a quantidade de km percorrido? '))
d = float(input('Quantos dias foi alugado? '))
v = (km*0.15)+(d*60)
print('O preço do aluguel foi: R${:.2f}'.format(v))

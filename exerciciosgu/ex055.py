maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
     p = int(input('Qual o {} peso: '.format(c)))
     if p > maiorpeso : maiorpeso = p
     if menorpeso == 0 : menorpeso = p
     elif p < menorpeso : menorpeso = p
print('''O maior peso é: {}
e o menor é: {}'''.format(maiorpeso, menorpeso))
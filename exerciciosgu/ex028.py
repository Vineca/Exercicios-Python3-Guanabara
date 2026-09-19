import random
numero = random.randint(0,5)
descobrir = int(input('Qual numero que eu pensei de 0 a 5? '))
#print('Você venceu') if descobrir == numero else print('Você perdeu')
print('voce venceu'if descobrir == numero else 'voce perdeu')


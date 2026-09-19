import random
numero = random.randint(0,10)
chute = ''
tentativas = 0
while numero != chute:
    chute = int(input('Qual o numero que eu pensei?'))
    print('tente outra vez OTARIO!')
    tentativas = tentativas + 1
print('voce acertou, o numero realmente é {} depois de tentar {}'.format(numero,tentativas))

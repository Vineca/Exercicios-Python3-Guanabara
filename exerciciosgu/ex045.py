import random
computador = random.choice(['Pedra','Papel','Tesoura']).upper()
jogador = input('Pedra, Papel ou Tesoura?').upper()
if jogador == computador: print('{} = {} então EMPATOU'.format(jogador, computador))
elif jogador == 'PEDRA' and computador == 'TESOURA': print('Computador {} , Jogador {} então Jogador venceu'.format(computador, jogador))
elif jogador == 'PAPEL' and computador == 'PEDRA': print('Computador {} , Jogador {} então Jogador venceu'.format(computador, jogador))
elif jogador == 'TESOURA' and computador == 'PEDRA': print('Computador {} , Jogador {} então Jogador venceu'.format(computador, jogador))
else: print('Computador {} , Jogador {} então Computador venceu'.format(computador, jogador))
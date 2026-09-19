nome = str(input('Qual o seu nome: '))
partidas = {}
partidas[nome] = {}
jogos = int(input('Quantos jogos perna de pau? '))
total = 0
for c in range(1,jogos+1):
    partidas[nome][c] = int(input(f'Quantos gols no jogo {c}: '))
    total += int(partidas[nome][c])
partidas[nome]['Total'] = total
# print(partidas.values())
# print(partidas[nome]['Total'])
# print(partidas.items())

for k,v in partidas.items():
    print(f'Nome: {k}')
    print('Gols: [', end='')
    for a,b in v.items():
        if a != 'Total':
            print(f'{b}, ', end='')
    print(']')
print(f'Total de gols: {partidas[nome]['Total']}')
print()
for k, v in partidas[nome].items():
    if k != 'Total':
        print(f'O jogo {k} fez {v} gols.')
    else:
        print(f'{k} de {v} gols.')


continuar = 0
lista = []
while continuar != 'N':
    partidas = {}
    total = 0
    partidas['nome'] = str(input('Qual o seu nome: '))
    jogos = int(input('Quantos jogos perna de pau? '))
    partidas['gols'] = []
    for c in range(1,jogos+1):
        partidas['gols'].append(int(input(f'Quantos gols no jogo {c}: ')))
    partidas['Total'] = sum(partidas['gols'])
    lista.append(partidas.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
print(lista)
for n,jog in enumerate(lista):
    print(f'O jogador {n} : Nome: {jog['nome']}')
    for l,g in enumerate(jog['gols'], start=1):
        print(f'No jogo {l} fez {g} gols')
    print(f'E teve um total de gols: {sum(jog['gols'])}')
jogador = int(input('Qual jogador [999=quit]: '))
while jogador != 999:
    if 0 <= jogador < len(lista):
        for k,v in lista[jogador].items():
            if k == 'gols':
                for pa,go in enumerate(v, start=1):
                    print(f'No jogo {pa} fez {go} gols')
        jogador = int(input('Qual jogador [999=quit]: '))
    else: jogador = int(input('Jogador não existe burro, qual jogador [999=quit]: '))




# print(partidas.values())
# print(partidas[nome]['Total'])
# print(partidas.items())

# for k,v in partidas.items():
#     print(f'Nome: {k}')
#     print('Gols: [', end='')
#     for a,b in v.items():
#         if a != 'Total':
#             print(f'{b}, ', end='')
#     print(']')
# print(f'Total de gols: {partidas[nome]['Total']}')
# print()
# for k, v in partidas[nome].items():
#     if k != 'Total':
#         print(f'O jogo {k} fez {v} gols.')
#     else:
#         print(f'{k} de {v} gols.')


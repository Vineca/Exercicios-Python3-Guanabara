continuar = 0
lista = []
while continuar != 'N':
    partidas = {}
    total = 0
    partidas['nome'] = str(input('Qual o seu nome: '))
    jogos = int(input('Quantos jogos perna de pau? '))
    for c in range(1,jogos+1):
        partidas[c] = int(input(f'Quantos gols no jogo {c}: '))
        total += int(partidas[c])
    partidas['Total'] = total
    lista.append(partidas.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
print(lista)
for n,jog in enumerate(lista):
    print(f'{n}, {jog["nome"]}')

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


linhas = [[], [], []]
for c in range(0, 3):
    digite = int(input(f'elemento (0,{c}): '))
    linhas[0].append(digite)
for c in range(0, 3):
    digite = int(input(f'elemento (1,{c}): '))
    linhas[1].append(digite)
for c in range(0, 3):
    digite = int(input(f'elemento (2,{c}): '))
    linhas[2].append(digite)
print(linhas[0])
print(linhas[1])
print(linhas[2])
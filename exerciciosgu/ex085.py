listar = [[], []]
for c in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        listar[0].append(num)
    else:
        listar[1].append(num)
listar[0].sort()
listar[1].sort()
print(listar[0])
print(listar[1])

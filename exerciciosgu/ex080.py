lista = [int(input('Digite um valor: '))]

for c in range(0, 4):
    num = int(input('Digite um valor: '))
    if num > max(lista):
        lista.append(num)
    # elif num < min(lista):
    #     lista.insert(0, num)
    else:
        for d in range(0, len(lista)):
            if num <= lista[d]:
                lista.insert(d,num)
                break

print(lista)
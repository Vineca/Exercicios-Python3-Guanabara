lista = []
posi_maior = []
posi_menor = []
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
for posi,numero in enumerate(lista):
    if numero == max(lista):
        posi_maior.append(posi)
    if numero == min(lista):
        posi_menor.append(posi)
print(max(lista))
print(posi_maior)
print()
print(min(lista))
print(posi_menor)

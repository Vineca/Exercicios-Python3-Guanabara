s=0
for c in range(1,500):
    if c % 3 == 0 and c % 2 != 0:
        s+=c
print('a soma de todos os numeros impares entre 1 e 500 é:',s)

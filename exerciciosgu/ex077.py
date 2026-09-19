lista = ('palavra','bunda-mole','betinha','malandro','safada','abacaxi')
for c in lista:
    l=0
    print(f'na palavra {c} temos ', end='')
    while l != len(c):
        if c[l] in 'aeiou': print(c[l], end=' ')
        l += 1
    print()

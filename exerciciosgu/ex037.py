numero1 = int(input('digite um numero inteiro: '))
base = int(input('Digite \n 1 para binario \n 2 para octal \n 3 para hexadecimal: '))
if base == 1: print(bin(numero1)[2:])
elif base == 2: print(oct(numero1)[2:])
elif base == 3: print(hex(numero1)[2:])
else:
    print('A base digitada não é valida')

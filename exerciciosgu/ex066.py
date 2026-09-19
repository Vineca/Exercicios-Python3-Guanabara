cont = soma = num = 0
while True:
    num = int(input('Digite um numero vagabundo: '))
    if num == 999 : break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e sua soma é {soma}')

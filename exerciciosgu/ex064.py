soma = 0
n = 0
numero = int(input('Digite um numero inteiro: '))
while numero != 999:
    soma += numero
    n += 1
    numero = int(input('Digite um numero inteiro: '))
print(soma)
print(n)
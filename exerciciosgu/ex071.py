valor = int(input('Qual valor deseja sacar pau no cu? '))
nota50 = nota20 = nota10 = nota1 = 0
import math
while True:
    if valor/50 >= 1:
        nota50 = math.floor(valor/50)
        valor = valor%50
    if valor/20 >= 1:
        nota20 = math.floor(valor/20)
        valor = valor%20
    if valor/10 >= 1:
        nota10 = math.floor(valor/10)
        valor = valor%10
    if valor/1 >= 1:
        nota1 = math.floor(valor/1)
    break
print(nota50)
print(nota20)
print(nota10)
print(nota1)
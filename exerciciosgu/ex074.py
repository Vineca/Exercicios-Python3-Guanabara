from random import randint
a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
lista = a,b,c,d,e
print(lista)
menor = maior = a
for c in lista:
 if c > maior: maior = c
 if c < menor: menor = c
print(maior)
print(menor)

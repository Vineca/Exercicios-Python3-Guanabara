a = int(input('1 reta: '))
b = int(input('2 reta: '))
c = int(input('3 reta: '))
lado1 = a + b > c
lado2 = c + a > b
lado3 = b + c > a
tipo = 'isoceles'
if a == b == c: tipo = 'equilatero'
elif a != b != c != a: tipo = 'escaleno'
if lado1 == lado2 == lado3 == 1: print('As retas formam um triangulo {}'.format(tipo))
else: print('As retas não formam um triangulo')